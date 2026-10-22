/* Salt Services — particle-morph hero (adapted from Weblove Template 20).
   14,000 particles fly in and form the Salt hand (its falling salt in amber, as in
   The Salt Effect), then cycle sphere → "SALT" → ring → hand, and flee the cursor.
   Brand colors: bone-white grains with 14% amber sparks on the navy hero.
   The swarm is offset to the right half so the headline stays readable;
   desktop pointers only, skipped for reduced-motion — the static gradient
   hero underneath is the fallback for everyone else (and for crawlers). */
import * as THREE from 'three';

const MORPH_WORD = 'SALT';      /* SLOT: MORPH_WORD */
const N = 14000;                /* SLOT: PARTICLE_COUNT */

const mount = document.getElementById('hero-scene');
if (mount &&
    matchMedia('(pointer:fine)').matches &&
    matchMedia('(prefers-reduced-motion: no-preference)').matches &&
    innerWidth >= 900) {
  try {
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    const size = () => [mount.clientWidth, mount.clientHeight];
    renderer.setSize(...size());
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    mount.appendChild(renderer.domElement);
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, mount.clientWidth / mount.clientHeight, .1, 100);
    camera.position.z = 11;

    /* ---------- three target shapes ---------- */
    function sphereTargets() {
      const a = new Float32Array(N * 3);
      for (let i = 0; i < N; i++) {
        const phi = Math.acos(2 * Math.random() - 1), th = Math.random() * Math.PI * 2, r = 2.2;
        a[i * 3] = r * Math.sin(phi) * Math.cos(th);
        a[i * 3 + 1] = r * Math.cos(phi);
        a[i * 3 + 2] = r * Math.sin(phi) * Math.sin(th);
      }
      return a;
    }
    function ringTargets() {
      const a = new Float32Array(N * 3);
      for (let i = 0; i < N; i++) {
        const th = Math.random() * Math.PI * 2, tube = Math.random() * Math.PI * 2, R = 2.0, r = .6;
        a[i * 3] = (R + r * Math.cos(tube)) * Math.cos(th);
        a[i * 3 + 1] = r * Math.sin(tube);
        a[i * 3 + 2] = (R + r * Math.cos(tube)) * Math.sin(th);
      }
      return a;
    }
    function textTargets(word) {
      const cw = 900, ch = 240, cv = document.createElement('canvas');
      cv.width = cw; cv.height = ch;
      const c2 = cv.getContext('2d');
      c2.fillStyle = '#000'; c2.fillRect(0, 0, cw, ch);
      c2.fillStyle = '#fff';
      c2.font = `600 ${word.length > 6 ? 150 : 190}px Fraunces, Georgia, serif`;
      c2.textAlign = 'center'; c2.textBaseline = 'middle';
      c2.fillText(word, cw / 2, ch / 2);
      const px = c2.getImageData(0, 0, cw, ch).data, pts2 = [];
      for (let y = 0; y < ch; y += 2) for (let x = 0; x < cw; x += 2)
        if (px[(y * cw + x) * 4] > 128) pts2.push([(x - cw / 2) / 90, -(y - ch / 2) / 90]);
      const a = new Float32Array(N * 3);
      for (let i = 0; i < N; i++) {
        const p = pts2[Math.floor(Math.random() * pts2.length)] || [0, 0];
        a[i * 3] = p[0] + (Math.random() - .5) * .05;
        a[i * 3 + 1] = p[1] + (Math.random() - .5) * .05;
        a[i * 3 + 2] = (Math.random() - .5) * .4;
      }
      return a;
    }

    /* the Salt hand, from the logo: the hand in bone-white grains, the falling salt (the
       small separate shapes in the logo) in the amber sparks */
    const spark = new Uint8Array(N);
    for (let i = 0; i < N; i++) spark[i] = Math.random() < .14 ? 1 : 0;  /* SLOT: 14% amber sparks */
    const logo = await new Promise(res => {
      const im = new Image();
      im.onload = () => res(im); im.onerror = () => res(null);
      im.src = '/images/salt-logo.png';
      setTimeout(() => res(null), 4000);
    });
    function handTargets(img) {
      const S = 300, cv = document.createElement('canvas');
      cv.width = cv.height = S;
      const c2 = cv.getContext('2d');
      c2.drawImage(img, 0, 0, S, S);
      const px = c2.getImageData(0, 0, S, S).data;
      const lab = new Int32Array(S * S).fill(-1), sizes = [], stack = [];
      for (let i = 0; i < S * S; i++) {
        if (lab[i] !== -1 || px[i * 4 + 3] < 100) continue;
        const id = sizes.length; let n = 0; stack.push(i); lab[i] = id;
        while (stack.length) {
          const j = stack.pop(); n++;
          const x = j % S, y = (j / S) | 0;
          for (const k of [x > 0 ? j - 1 : -1, x < S - 1 ? j + 1 : -1, y > 0 ? j - S : -1, y < S - 1 ? j + S : -1])
            if (k >= 0 && lab[k] === -1 && px[k * 4 + 3] >= 100) { lab[k] = id; stack.push(k); }
        }
        sizes.push(n);
      }
      const hand = [], grains = [], grainMax = S * S * .004;
      for (let i = 0; i < S * S; i++) if (lab[i] !== -1)
        (sizes[lab[i]] < grainMax ? grains : hand).push([((i % S) - S / 2) / 60, -(((i / S) | 0) - S / 2) / 60]);
      if (!hand.length) return null;
      const a = new Float32Array(N * 3);
      for (let i = 0; i < N; i++) {
        const from = spark[i] && grains.length ? grains : hand;
        const p = from[Math.floor(Math.random() * from.length)];
        a[i * 3] = p[0] + (Math.random() - .5) * .03;
        a[i * 3 + 1] = p[1] + (Math.random() - .5) * .03;
        a[i * 3 + 2] = (Math.random() - .5) * .3;
      }
      return a;
    }
    const handData = logo && handTargets(logo);

    const TARGETS = [
      ...(handData ? [{ name: 'HAND', data: handData, hold: 9000 }] : []),
      { name: 'SPHERE', data: sphereTargets() },
      { name: MORPH_WORD, data: textTargets(MORPH_WORD) }, /* first pass (fallback font ok) */
      { name: 'RING', data: ringTargets() }
    ];
    const wordT = TARGETS.find(x => x.name === MORPH_WORD);
    document.fonts.ready.then(() => { wordT.data = textTargets(MORPH_WORD); });

    /* ---------- particle buffers ---------- */
    const pos = new Float32Array(N * 3), col = new Float32Array(N * 3);
    if (handData) {
      /* start scattered well outside the frame, so the grains fly in and gather into the hand */
      for (let i = 0; i < N; i++) {
        const a = Math.random() * Math.PI * 2, r = 7 + Math.random() * 6;
        pos[i * 3] = Math.cos(a) * r; pos[i * 3 + 1] = Math.sin(a) * r * .7; pos[i * 3 + 2] = (Math.random() - .5) * 4;
      }
    } else pos.set(TARGETS[0].data);
    for (let i = 0; i < N; i++) {
      col[i * 3] = spark[i] ? .91 : .93;      /* amber sparks, rest bone-white */
      col[i * 3 + 1] = spark[i] ? .63 : .92;
      col[i * 3 + 2] = spark[i] ? .23 : .87;
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
    const pts = new THREE.Points(geo, new THREE.PointsMaterial({ size: .035, vertexColors: true, transparent: true, opacity: .92 }));
    /* keep the swarm right of the headline at any viewport width,
       scaled so the word (span ~±2.8 + wobble) never clips the edge */
    function placeSwarm() {
      const halfW = Math.tan(camera.fov * Math.PI / 360) * camera.position.z * camera.aspect;
      pts.position.x = Math.max(2.6, halfW - 3.0);
      const room = halfW - pts.position.x - 0.6;
      pts.scale.setScalar(Math.min(1, Math.max(.6, room / 2.8)));
    }
    placeSwarm();
    scene.add(pts);

    /* ---------- morph cycle + cursor repel ---------- */
    let ti = 0;
    const shapeEl = document.getElementById('shape');
    if (shapeEl) shapeEl.textContent = TARGETS[0].name;
    (function next() {
      setTimeout(() => {
        ti = (ti + 1) % TARGETS.length;
        if (shapeEl) shapeEl.textContent = TARGETS[ti].name;
        next();
      }, TARGETS[ti].hold || 5000);   /* the hand holds longer than the other shapes */
    })();

    const mouse = new THREE.Vector2(-99, -99); /* far away = no repel until the mouse moves */
    let rotX = 0;                              /* rotation input starts neutral, not at -99 */
    const ray = new THREE.Raycaster(), plane = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0), hit = new THREE.Vector3();
    addEventListener('mousemove', e => {
      const r = mount.getBoundingClientRect();
      mouse.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
      rotX = mouse.x;
    });
    addEventListener('resize', () => {
      const [w, h] = size();
      camera.aspect = w / h; camera.updateProjectionMatrix();
      renderer.setSize(w, h);
      placeSwarm();
    });

    const clock = new THREE.Clock();
    let hidden = false;
    document.addEventListener('visibilitychange', () => { hidden = document.hidden; });
    (function loop() {
      requestAnimationFrame(loop);
      if (hidden) return;
      const t = clock.getElapsedTime();
      ray.setFromCamera(mouse, camera);
      ray.ray.intersectPlane(plane, hit);
      /* hit in the swarm's local (translated + scaled) space */
      const k = pts.scale.x, hx = (hit.x - pts.position.x) / k, hy = hit.y / k;
      const target = TARGETS[ti].data, p = geo.attributes.position.array;
      for (let i = 0; i < N; i++) {
        const ix = i * 3;
        /* pull toward target */
        p[ix]     += (target[ix]     - p[ix])     * .045;
        p[ix + 1] += (target[ix + 1] - p[ix + 1]) * .045;
        p[ix + 2] += (target[ix + 2] - p[ix + 2]) * .045;
        /* cursor repulsion */
        const dx = p[ix] - hx, dy = p[ix + 1] - hy;
        const d2 = dx * dx + dy * dy;
        if (d2 < 2.2) {
          const f = (2.2 - d2) * .06 / Math.sqrt(d2 + .0001);
          p[ix] += dx * f; p[ix + 1] += dy * f;
        }
        /* breath */
        p[ix + 2] += Math.sin(t + i) * .0006;
      }
      geo.attributes.position.needsUpdate = true;
      pts.rotation.y = Math.sin(t * .1) * .25 + rotX * .18;
      renderer.render(scene, camera);
    })();

    mount.classList.add('on');
    mount.closest('.hero-3d').classList.add('scene-on');
  } catch (e) {
    /* WebGL unavailable — the static gradient hero stays */
  }
}
