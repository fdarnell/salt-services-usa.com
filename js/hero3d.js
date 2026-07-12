/* Salt Services — interactive 3D hero (adapted from Weblove Template 05, Route B).
   Brand-recolored: navy scene, chrome knot, amber rim + amber icosahedron.
   Desktop pointers only, skipped for reduced-motion; the static gradient hero
   underneath is the fallback for everyone else (and for crawlers). */
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const mount = document.getElementById('hero-scene');
if (mount &&
    matchMedia('(pointer:fine)').matches &&
    matchMedia('(prefers-reduced-motion: no-preference)').matches &&
    innerWidth >= 900) {
  try {
    const mouse = { x: 0, y: 0 };
    addEventListener('mousemove', e => {
      mouse.x = e.clientX / innerWidth - .5;
      mouse.y = e.clientY / innerHeight - .5;
    });

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    const size = () => [mount.clientWidth, mount.clientHeight];
    renderer.setSize(...size());
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    mount.appendChild(renderer.domElement);

    const scene = new THREE.Scene();
    scene.fog = new THREE.Fog(0x0e1f38, 6, 16);
    const camera = new THREE.PerspectiveCamera(42, mount.clientWidth / mount.clientHeight, .1, 50);
    camera.position.set(0, 0, 7);
    scene.environment = new THREE.PMREMGenerator(renderer)
      .fromScene(new RoomEnvironment(), .04).texture;

    const key = new THREE.PointLight(0xfff2e0, 30); key.position.set(4, 3, 4); scene.add(key);
    const rim = new THREE.PointLight(0xe9a13b, 60); rim.position.set(-5, -2, -3); scene.add(rim);

    const knot = new THREE.Mesh(
      new THREE.TorusKnotGeometry(1.35, .42, 260, 40),
      new THREE.MeshPhysicalMaterial({ color: 0x1a2436, metalness: 1, roughness: .12, clearcoat: 1, clearcoatRoughness: .25 })
    );
    knot.position.x = 2.1; scene.add(knot);

    const ico = new THREE.Mesh(
      new THREE.IcosahedronGeometry(.5, 0),
      new THREE.MeshPhysicalMaterial({ color: 0xe9a13b, metalness: .4, roughness: .25, emissive: 0x3d2605 })
    );
    ico.position.set(3.9, 1.6, -1); scene.add(ico);

    /* salt-grain dust */
    const n = 350, pos = new Float32Array(n * 3);
    for (let i = 0; i < n * 3; i++) pos[i] = (Math.random() - .5) * 18;
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    const dust = new THREE.Points(geo, new THREE.PointsMaterial({ color: 0x8fa3c0, size: .02, transparent: true, opacity: .7 }));
    scene.add(dust);

    addEventListener('resize', () => {
      const [w, h] = size();
      camera.aspect = w / h; camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });

    const clock = new THREE.Clock();
    (function loop() {
      requestAnimationFrame(loop);
      const t = clock.getElapsedTime();
      knot.rotation.x = t * .18 + mouse.y * .5;
      knot.rotation.y = t * .24 + mouse.x * .8;
      ico.rotation.x = t * .5; ico.rotation.y = t * .4;
      ico.position.y = 1.6 + Math.sin(t * 1.2) * .2;
      dust.rotation.y = t * .02;
      camera.position.x = mouse.x * .9;
      camera.position.y = -mouse.y * .7;
      camera.lookAt(1.4, 0, 0);
      renderer.render(scene, camera);
    })();

    mount.classList.add('on');
  } catch (e) {
    /* WebGL unavailable — the static gradient hero stays */
  }
}
