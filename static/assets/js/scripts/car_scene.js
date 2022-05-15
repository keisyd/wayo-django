import * as THREE from "../../static/js/three.module.js";
import { OrbitControls } from "../../static/js/OrbitControls.js";
import { GLTFLoader } from "../../static/js/GLTFLoader.js";
let scene, camera, renderer;
var model;

function init() {
  renderer = new THREE.WebGLRenderer({ antialias: true });
  var container = document.getElementById("canvas");
  var w = container.offsetWidth;
  var h = container.offsetHeight;

  renderer.setSize(w, h);

  scene = new THREE.Scene();
  scene.background = new THREE.Color(0xdddddd);

  camera = new THREE.PerspectiveCamera(
    50,
    window.innerWidth / window.innerHeight,
    1,
    5000
  );
  camera.rotation.y = (45 / 180) * Math.PI;
  camera.position.x = 800;
  camera.position.y = 100;
  camera.position.z = 1000;

  //let controls = new OrbitControls(camera, renderer.domElement);
  //controls.addEventListener("change", renderer);

  let hlight = new THREE.AmbientLight(0x404040, 100);
  scene.add(hlight);

  let directionalLight = new THREE.DirectionalLight(0xffffff, 100);
  directionalLight.position.set(0, 1, 0);
  directionalLight.castShadow = true;
  scene.add(directionalLight);
  let light = new THREE.PointLight(0xc4c4c4, 10);
  light.position.set(0, 300, 500);
  scene.add(light);
  let light2 = new THREE.PointLight(0xc4c4c4, 10);
  light2.position.set(500, 100, 0);
  scene.add(light2);
  let light3 = new THREE.PointLight(0xc4c4c4, 10);
  light3.position.set(0, 100, -500);
  scene.add(light3);
  let light4 = new THREE.PointLight(0xc4c4c4, 10);
  light4.position.set(-500, 300, 500);
  scene.add(light4);

  //document.body.appendChild(renderer.domElement);
  container.appendChild(renderer.domElement);

  let loader = new GLTFLoader();
  loader.load("../../static/assets/3d/scene.gltf", function (gltf) {
    let car = gltf.scene.children[0];
    car.scale.set(0.5, 0.5, 0.5);

    model = gltf.scene;

    scene.add(model);
    animate();
  });
}

function animate() {
  render();

  requestAnimationFrame(animate);
}

function render() {
  model.rotation.y += 0.01;

  renderer.render(scene, camera);
}

init();