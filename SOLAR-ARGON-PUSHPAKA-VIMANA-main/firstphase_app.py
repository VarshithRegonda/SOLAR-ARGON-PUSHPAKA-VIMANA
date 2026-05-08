from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Pushpaka Vimana — Flight Sim</title>
<style>
body { margin:0; overflow:hidden; background:black; color:white; font-family:Arial; }

#hud {
  position:absolute;
  top:10px;
  left:10px;
  background:rgba(0,0,0,0.6);
  padding:10px;
  font-size:13px;
}

#controls {
  position:absolute;
  bottom:10px;
  left:10px;
}
button { margin:3px; padding:6px; }
</style>

<script src="https://cdn.jsdelivr.net/npm/three@0.158/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.158/examples/js/controls/OrbitControls.js"></script>
</head>

<body>

<div id="hud">
Speed: <span id="speed">0</span><br>
Altitude: <span id="alt">0</span><br>
Lift: <span id="lift">0</span><br>
Drag: <span id="drag">0</span><br>
AoA: <span id="aoa">0</span>
</div>

<div id="controls">
<button onclick="toggle('airflow')">AIRFLOW</button>
</div>

<script>
// Scene
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.set(0,3,8);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new THREE.OrbitControls(camera, renderer.domElement);

// Drone
const drone = new THREE.Mesh(
  new THREE.BoxGeometry(2,0.3,1),
  new THREE.MeshStandardMaterial({color:0xc9a84c, wireframe:true})
);
scene.add(drone);

// Light
const light = new THREE.DirectionalLight(0xffffff,1);
light.position.set(5,5,5);
scene.add(light);

// Physics
let velocity = new THREE.Vector3(0,0,0);
let thrust = 0;
let lift = 0;
let drag = 0;

const gravity = -0.01;

// Input
let keys = {};
window.addEventListener("keydown", e=>keys[e.key]=true);
window.addEventListener("keyup", e=>keys[e.key]=false);

// Airflow
const airflow = new THREE.Group();
for(let i=0;i<150;i++){
  const p = new THREE.Mesh(
    new THREE.SphereGeometry(0.03),
    new THREE.MeshBasicMaterial({color:0x00ffff})
  );
  p.position.set(Math.random()*10-5, Math.random()*2, Math.random()*2-1);
  airflow.add(p);
}
scene.add(airflow);

function toggle(type){
  if(type==="airflow") airflow.visible = !airflow.visible;
}

// Physics update
function updatePhysics(){

  if(keys["w"]) thrust += 0.002;
  if(keys["s"]) thrust -= 0.002;
  thrust = Math.max(0, Math.min(thrust, 0.1));

  if(keys["ArrowUp"]) drone.rotation.x -= 0.02;
  if(keys["ArrowDown"]) drone.rotation.x += 0.02;

  let forward = new THREE.Vector3(0,0,-1).applyQuaternion(drone.quaternion);

  lift = velocity.length() * 0.05;
  drag = velocity.length() * 0.02;

  velocity.y += gravity;
  velocity.add(forward.multiplyScalar(thrust));
  velocity.y += lift;

  velocity.multiplyScalar(0.99);
  drone.position.add(velocity);

  if(drone.position.y < 0){
    drone.position.y = 0;
    velocity.y = 0;
  }
}

// Loop
function animate(){
  requestAnimationFrame(animate);

  updatePhysics();

  airflow.children.forEach(p=>{
    p.position.addScaledVector(velocity, -0.5);
    if(p.position.x < -5) p.position.x = 5;
  });

  document.getElementById("speed").innerText = velocity.length().toFixed(2);
  document.getElementById("alt").innerText = drone.position.y.toFixed(2);
  document.getElementById("lift").innerText = lift.toFixed(2);
  document.getElementById("drag").innerText = drag.toFixed(2);
  document.getElementById("aoa").innerText = (drone.rotation.x*57).toFixed(1);

  controls.update();
  renderer.render(scene, camera);
}

animate();

window.addEventListener("resize", ()=>{
  camera.aspect = window.innerWidth/window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    print("🚀 Open http://localhost:5000")
    app.run(debug=True)
