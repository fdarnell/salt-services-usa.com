/**
 * POST /api/intake — receives a client-intake submission from /intake/,
 * stores it privately in Vercel Blob, and (optionally) forwards it to a
 * Coraline inbound webhook.
 *
 * Env vars (Vercel project settings):
 *   BLOB_READ_WRITE_TOKEN  — added automatically when Blob storage is created
 *   INTAKE_CODE            — shared access code the page must send
 *   CORALINE_WEBHOOK_URL   — optional; if set, each submission is forwarded
 *
 * GET /api/intake?code=...  — lists stored submissions (used by the local sync
 * script so Claude sessions can pull them into ~/Downloads/client-intake).
 */
import { put, list, get, del } from '@vercel/blob';

function slug(s) {
  return String(s || 'client').toLowerCase().replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '').slice(0, 60) || 'client';
}

export default async function handler(req, res) {
  // CORS: the Claude artifact version of this worksheet posts from another
  // origin. The access code — not the origin — is the security boundary here.
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS");
  res.setHeader('Access-Control-Allow-Headers', 'content-type, x-intake-code');
  res.setHeader('Access-Control-Max-Age', '86400');
  if (req.method === 'OPTIONS') return res.status(204).end();

  const code = req.headers['x-intake-code'] || req.query.code;
  if (!process.env.INTAKE_CODE || code !== process.env.INTAKE_CODE) {
    return res.status(401).json({ error: 'bad or missing access code' });
  }

  if (req.method === 'GET') {
    try {
      const { blobs } = await list({ prefix: 'intake/' });
      const wanted = blobs.sort((a, b) => new Date(b.uploadedAt) - new Date(a.uploadedAt));
      const detail = req.query.full === '1'
        ? await Promise.all(wanted.map(async b => {
            // private store: read content through the SDK's stream, not the raw URL
            const result = await get(b.pathname, { access: 'private' });
            let data = null;
            if (result && result.stream) {
              const text = await new Response(result.stream).text();
              try { data = JSON.parse(text); } catch { data = { raw: text }; }
            }
            return { pathname: b.pathname, uploadedAt: b.uploadedAt, data };
          }))
        : wanted.map(b => ({ pathname: b.pathname, uploadedAt: b.uploadedAt }));
      return res.status(200).json({ count: detail.length, submissions: detail });
    } catch (err) {
      const msg = String(err.message || err);
      if (/No token found|BLOB_READ_WRITE_TOKEN/i.test(msg)) {
        // code is valid but storage isn't wired yet — let the page unlock anyway
        return res.status(200).json({ count: 0, submissions: [], warning: 'storage not configured' });
      }
      return res.status(500).json({ error: 'list failed', detail: msg });
    }
  }

  if (req.method === 'DELETE') {
    const pathname = req.query.pathname;
    if (!pathname || !String(pathname).startsWith('intake/')) {
      return res.status(400).json({ error: 'pathname query param required' });
    }
    try {
      await del(pathname);
      return res.status(200).json({ ok: true, deleted: pathname });
    } catch (err) {
      return res.status(500).json({ error: 'delete failed', detail: String(err.message || err) });
    }
  }

  if (req.method !== 'POST') {
    res.setHeader('Allow', 'GET, POST, DELETE');
    return res.status(405).json({ error: 'method not allowed' });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch { return res.status(400).json({ error: 'invalid JSON' }); }
  }
  if (!body || typeof body !== 'object' || !body.biz) {
    return res.status(400).json({ error: 'missing business name' });
  }

  const now = new Date();
  const record = {
    ...body,
    submittedAt: now.toISOString(),
    source: 'saltservicesusa.com/intake/',
  };
  const stamp = now.toISOString().slice(0, 19).replace(/[:T]/g, '-');
  const pathname = `intake/${slug(body.biz)}-${stamp}.json`;

  try {
    const blob = await put(pathname, JSON.stringify(record, null, 2), {
      access: 'private',             // store is private; content is read back through the API
      contentType: 'application/json',
      addRandomSuffix: true,
    });

    let forwarded = null;
    if (process.env.CORALINE_WEBHOOK_URL) {
      try {
        const r = await fetch(process.env.CORALINE_WEBHOOK_URL, {
          method: 'POST',
          headers: { 'content-type': 'application/json' },
          body: JSON.stringify(record),
        });
        forwarded = r.status;
      } catch (e) {
        forwarded = 'error: ' + String(e.message || e);
      }
    }

    return res.status(200).json({ ok: true, stored: blob.pathname, forwarded });
  } catch (err) {
    const msg = String(err.message || err);
    if (/No token found|BLOB_READ_WRITE_TOKEN/i.test(msg)) {
      return res.status(503).json({
        error: 'storage not configured — add BLOB_READ_WRITE_TOKEN in Vercel project settings',
      });
    }
    return res.status(500).json({ error: 'store failed', detail: msg });
  }
}
