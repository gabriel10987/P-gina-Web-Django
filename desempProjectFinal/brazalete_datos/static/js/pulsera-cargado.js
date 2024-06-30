var renderer, scene, camera, myCanvas = document.getElementById('myCanvas');

//renderer
renderer = new THREE.WebGLRenderer({ canvas: myCanvas, antialias: true });
renderer.setClearColor(0x000000);
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);

//camera
camera = new THREE.PerspectiveCamera(35, window.innerWidth / window.innerHeight, 0.1, 1000);

//scene
scene = new THREE.Scene();

//Lights
var light  = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(light)

var light2  = new THREE.PointLight(0xffffff, 0.5);
scene.add(light2)

var loader = new THREE.GLTFLoader();
loader.load( 'prueba.glb', handle_load)

var mesh;

function handle_load(gltf) {
    mesh = gltf.scene.children[0];
    scene.add(mesh);
    mesh.position.z = -10;
}

//render loop
render();

var delta = 0;
var prevTime = Date.now();

function render(){
    delta += 0.01;

    if(mesh){
        mesh.rotation.y += 0.01;
    }

    renderer.render(scene, camera)

    requestAnimationFrame(render);
}