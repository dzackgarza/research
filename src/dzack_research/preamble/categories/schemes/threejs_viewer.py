r"""
Interactive Three.js 3D Polytope and Lattice Viewer.

Provides rich HTML/JavaScript 3D rendering with:
- Infinite anti-aliased shader grid (dual-frequency minor/major grid with radial fade)
- Seemingly infinite RGB coordinate axes with glow rays and tick markers
- Vast 3D integral lattice grid ZZ^3 rendered at 60+ FPS via THREE.InstancedMesh
- Jewel-like glassmorphic polytope facet shading with crisp glowing wireframe edges
- Game-style WASD + QE + Shift flight controls and smooth OrbitControls
- Translucent dark glass HUD with camera reset, full-screen toggle, and raycasting coordinate inspector
"""

import json
import uuid
from typing import Any, Mapping, Optional, Sequence

_TEMPLATE = """
<div id="__UID___wrapper" style="position: relative; width: 100%; height: __HEIGHT__px; background: #07090E; border-radius: 12px; overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #1E293B;">
    <!-- Three.js Canvas Container -->
    <div id="__UID___container" style="width: 100%; height: 100%; cursor: grab;"></div>

    <!-- HUD Overlay: Top Left Title & Info -->
    <div style="position: absolute; top: 14px; left: 16px; pointer-events: none; z-index: 10;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 15px; font-weight: 700; color: #F8FAFC; letter-spacing: 0.5px; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">__TITLE__</span>
            <span style="background: rgba(59, 130, 246, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); color: #93C5FD; font-size: 11px; font-weight: 600; padding: 2px 7px; border-radius: 9999px;">3D Interactive</span>
        </div>
        <div id="__UID___subtitle" style="font-size: 12px; color: #94A3B8; margin-top: 4px; text-shadow: 0 1px 3px rgba(0,0,0,0.8);">
            Lattice Polytope in N ⊕ ℤ | WASD + QE to Fly
        </div>
    </div>

    <!-- HUD Overlay: Top Right Action Toolbar -->
    <div style="position: absolute; top: 14px; right: 16px; display: flex; gap: 6px; z-index: 10;">
        <button id="__UID___btn_orbit" title="Toggle Auto-Rotation" style="background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.12); color: #E2E8F0; padding: 6px 10px; border-radius: 6px; font-size: 12px; font-weight: 500; cursor: pointer; transition: all 0.2s;">
            ↻ Auto-Spin
        </button>
        <button id="__UID___btn_grid" title="Toggle ZZ^3 Lattice Grid" style="background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.12); color: #E2E8F0; padding: 6px 10px; border-radius: 6px; font-size: 12px; font-weight: 500; cursor: pointer; transition: all 0.2s;">
            ▦ Grid
        </button>
        <button id="__UID___btn_axes" title="Toggle Coordinate Axes" style="background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.12); color: #E2E8F0; padding: 6px 10px; border-radius: 6px; font-size: 12px; font-weight: 500; cursor: pointer; transition: all 0.2s;">
            XYZ
        </button>
        <button id="__UID___btn_reset" title="Reset Camera View" style="background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.12); color: #E2E8F0; padding: 6px 10px; border-radius: 6px; font-size: 12px; font-weight: 500; cursor: pointer; transition: all 0.2s;">
            ⌂ Reset
        </button>
        <button id="__UID___btn_fs" title="Toggle Fullscreen" style="background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.12); color: #E2E8F0; padding: 6px 10px; border-radius: 6px; font-size: 12px; font-weight: 500; cursor: pointer; transition: all 0.2s;">
            ⛶
        </button>
    </div>

    <!-- HUD Overlay: Bottom Left Flight Navigation Guide -->
    <div style="position: absolute; bottom: 14px; left: 16px; background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.08); padding: 8px 12px; border-radius: 8px; font-size: 11px; color: #94A3B8; pointer-events: none; z-index: 10;">
        <div style="display: flex; gap: 12px; align-items: center;">
            <div><kbd style="background: #1E293B; color: #F1F5F9; padding: 1px 5px; border-radius: 3px; font-family: monospace; border: 1px solid #334155;">W A S D</kbd> Move</div>
            <div><kbd style="background: #1E293B; color: #F1F5F9; padding: 1px 5px; border-radius: 3px; font-family: monospace; border: 1px solid #334155;">Q / E</kbd> Up / Down</div>
            <div><kbd style="background: #1E293B; color: #F1F5F9; padding: 1px 5px; border-radius: 3px; font-family: monospace; border: 1px solid #334155;">Shift</kbd> Turbo</div>
            <div><kbd style="background: #1E293B; color: #F1F5F9; padding: 1px 5px; border-radius: 3px; font-family: monospace; border: 1px solid #334155;">Drag</kbd> Orbit/Pan</div>
        </div>
    </div>

    <!-- HUD Overlay: Bottom Right Inspector Tooltip -->
    <div id="__UID___inspector" style="position: absolute; bottom: 14px; right: 16px; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); border: 1px solid rgba(59, 130, 246, 0.3); padding: 8px 14px; border-radius: 8px; font-size: 11.5px; color: #E2E8F0; pointer-events: none; z-index: 10; min-width: 140px; text-align: right;">
        <span style="color: #38BDF8; font-weight: 600;">Hover Inspector:</span> Ready
    </div>
</div>

<script>
(function() {
    const payload = __PAYLOAD__;
    const wrapper = document.getElementById("__UID___wrapper");
    const container = document.getElementById("__UID___container");
    const inspector = document.getElementById("__UID___inspector");

    function loadScript(url) {
        return new Promise((resolve, reject) => {
            if (window.THREE && window.THREE.OrbitControls) {
                resolve();
                return;
            }
            const s = document.createElement("script");
            s.src = url;
            s.onload = resolve;
            s.onerror = reject;
            document.head.appendChild(s);
        });
    }

    async function init() {
        if (!window.THREE) {
            await loadScript("https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js");
        }
        if (!window.THREE.OrbitControls) {
            await loadScript("https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js");
        }
        startScene();
    }

    function startScene() {
        const width = container.clientWidth || 800;
        const height = container.clientHeight || 580;

        // 1. Scene & Atmosphere
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x07090E);
        scene.fog = new THREE.FogExp2(0x07090E, 0.015);

        // 2. Camera (Z-up coordinate system convention for toric math)
        const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
        camera.up.set(0, 0, 1);
        camera.position.set(7.5, -8.5, 6.0);

        // 3. WebGL Renderer
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
        renderer.setSize(width, height);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        container.appendChild(renderer.domElement);

        // 4. Orbit Controls
        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.06;
        controls.target.set(0.5, 0.5, 0.8);
        controls.maxDistance = 150;
        controls.minDistance = 0.5;

        // 5. Lighting Setup (Studio 3-Point + Ambient)
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.65);
        scene.add(ambientLight);

        const keyLight = new THREE.DirectionalLight(0xE0F2FE, 0.9);
        keyLight.position.set(15, -12, 20);
        scene.add(keyLight);

        const fillLight = new THREE.DirectionalLight(0x818CF8, 0.45);
        fillLight.position.set(-15, 12, 10);
        scene.add(fillLight);

        const rimLight = new THREE.DirectionalLight(0x38BDF8, 0.5);
        rimLight.position.set(0, 20, -10);
        scene.add(rimLight);

        // 6. Infinite Shader Grid Helper (Fyrestar-style anti-aliased ground plane)
        const gridVertexShader = `
            varying vec3 vWorldPos;
            uniform float uDistance;
            void main() {
                vec3 pos = position.xyz * uDistance;
                pos.xy += cameraPosition.xy;
                vWorldPos = pos;
                gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
            }
        `;
        const gridFragmentShader = `
            varying vec3 vWorldPos;
            uniform float uSize1;
            uniform float uSize2;
            uniform vec3 uColor;
            uniform float uDistance;

            float getGrid(float size) {
                vec2 r = vWorldPos.xy / size;
                vec2 grid = abs(fract(r - 0.5) - 0.5) / fwidth(r);
                float line = min(grid.x, grid.y);
                return 1.0 - min(line, 1.0);
            }

            void main() {
                float d = length(vWorldPos.xy - cameraPosition.xy);
                float alpha = 1.0 - smoothstep(0.05 * uDistance, uDistance, d);
                if (alpha <= 0.0) discard;

                float g1 = getGrid(uSize1);
                float g2 = getGrid(uSize2);
                float gridVal = max(g1 * 0.35, g2 * 0.85);
                if (gridVal <= 0.01) discard;

                gl_FragColor = vec4(uColor, gridVal * alpha * 0.55);
            }
        `;
        const gridGeo = new THREE.PlaneGeometry(2, 2, 1, 1);
        const gridMat = new THREE.ShaderMaterial({
            side: THREE.DoubleSide,
            transparent: true,
            uniforms: {
                uSize1: { value: 1.0 },
                uSize2: { value: 5.0 },
                uColor: { value: new THREE.Color(0x334155) },
                uDistance: { value: 200.0 }
            },
            vertexShader: gridVertexShader,
            fragmentShader: gridFragmentShader
        });
        const infiniteGrid = new THREE.Mesh(gridGeo, gridMat);
        infiniteGrid.position.z = 0;
        scene.add(infiniteGrid);

        // 7. Infinite Glowing Axis Rays (X=Red, Y=Green, Z=Blue)
        const axesGroup = new THREE.Group();
        const axisRadius = 0.022;
        const axisLength = 300.0;

        function createAxisRay(direction, colorHex, labelText) {
            const group = new THREE.Group();
            const geom = new THREE.CylinderGeometry(axisRadius, axisRadius, axisLength, 16);
            geom.translate(0, axisLength / 2, 0);

            const mat = new THREE.MeshStandardMaterial({
                color: colorHex,
                emissive: colorHex,
                emissiveIntensity: 0.45,
                roughness: 0.3
            });
            const cylinder = new THREE.Mesh(geom, mat);

            if (direction === 'x') {
                cylinder.rotation.z = -Math.PI / 2;
            } else if (direction === 'y') {
                // Default cylinder is along Y
            } else if (direction === 'z') {
                cylinder.rotation.x = Math.PI / 2;
            }
            group.add(cylinder);

            const negGeom = new THREE.CylinderGeometry(axisRadius * 0.7, axisRadius * 0.7, axisLength, 12);
            negGeom.translate(0, -axisLength / 2, 0);
            const negMat = new THREE.MeshBasicMaterial({ color: colorHex, opacity: 0.25, transparent: true });
            const negCylinder = new THREE.Mesh(negGeom, negMat);
            if (direction === 'x') negCylinder.rotation.z = -Math.PI / 2;
            else if (direction === 'z') negCylinder.rotation.x = Math.PI / 2;
            group.add(negCylinder);

            return group;
        }

        const xAxis = createAxisRay('x', 0xEF4444, 'X');
        const yAxis = createAxisRay('y', 0x22C55E, 'Y');
        const zAxis = createAxisRay('z', 0x3B82F6, 'Z');
        axesGroup.add(xAxis);
        axesGroup.add(yAxis);
        axesGroup.add(zAxis);
        scene.add(axesGroup);

        // 8. Vast 3D Lattice Grid ZZ^3 via InstancedMesh
        const L_RANGE = payload.latticeRange || 8;
        const sphereGeo = new THREE.SphereGeometry(1, 12, 12);

        const polyPointsSet = new Set();
        const interiorSet = new Set(payload.interiorPoints.map(p => `${p[0]},${p[1]},${p[2]}`));
        const vertexSet = new Set(payload.vertices.map(v => `${v[0]},${v[1]},${v[2]}`));
        const boundarySet = new Set(payload.boundaryPoints.map(p => `${p[0]},${p[1]},${p[2]}`));

        payload.vertices.forEach(v => polyPointsSet.add(`${v[0]},${v[1]},${v[2]}`));
        payload.interiorPoints.forEach(p => polyPointsSet.add(`${p[0]},${p[1]},${p[2]}`));
        payload.boundaryPoints.forEach(p => polyPointsSet.add(`${p[0]},${p[1]},${p[2]}`));

        const ambientPoints = [];
        for (let x = -L_RANGE; x <= L_RANGE; x++) {
            for (let y = -L_RANGE; y <= L_RANGE; y++) {
                for (let z = 0; z <= L_RANGE; z++) {
                    const key = `${x},${y},${z}`;
                    if (!polyPointsSet.has(key)) {
                        ambientPoints.push([x, y, z]);
                    }
                }
            }
        }

        const ambientMat = new THREE.MeshBasicMaterial({
            color: 0x64748B,
            transparent: true,
            opacity: 0.35
        });
        const ambientInstanced = new THREE.InstancedMesh(sphereGeo, ambientMat, ambientPoints.length);
        const dummy = new THREE.Object3D();
        ambientPoints.forEach((p, idx) => {
            dummy.position.set(p[0], p[1], p[2]);
            dummy.scale.set(0.035, 0.035, 0.035);
            dummy.updateMatrix();
            ambientInstanced.setMatrixAt(idx, dummy.matrix);
        });
        ambientInstanced.instanceMatrix.needsUpdate = true;
        scene.add(ambientInstanced);

        // 9. Polytope Facets Mesh (Jewel Glassmorphic Shading)
        const polyGroup = new THREE.Group();
        const verts = payload.vertices;

        const polyGeometry = new THREE.BufferGeometry();
        const positions = [];

        payload.facets.forEach(facetIndices => {
            if (facetIndices.length < 3) return;
            const fv = facetIndices.map(i => verts[i]);
            const p0 = fv[0];
            for (let i = 1; i < fv.length - 1; i++) {
                const p1 = fv[i];
                const p2 = fv[i + 1];
                positions.push(p0[0], p0[1], p0[2]);
                positions.push(p1[0], p1[1], p1[2]);
                positions.push(p2[0], p2[1], p2[2]);
            }
        });

        polyGeometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
        polyGeometry.computeVertexNormals();

        const polyMat = new THREE.MeshPhysicalMaterial({
            color: 0x38BDF8,
            emissive: 0x0369A1,
            emissiveIntensity: 0.18,
            roughness: 0.12,
            metalness: 0.1,
            transmission: 0.65,
            ior: 1.45,
            opacity: 0.72,
            transparent: true,
            side: THREE.DoubleSide,
            depthWrite: false
        });
        const polyMesh = new THREE.Mesh(polyGeometry, polyMat);
        polyGroup.add(polyMesh);

        // Polytope Wireframe Edges
        const edgePositions = [];
        payload.facets.forEach(facetIndices => {
            for (let i = 0; i < facetIndices.length; i++) {
                const v1 = verts[facetIndices[i]];
                const v2 = verts[facetIndices[(i + 1) % facetIndices.length]];
                edgePositions.push(v1[0], v1[1], v1[2], v2[0], v2[1], v2[2]);
            }
        });
        const edgeGeo = new THREE.BufferGeometry();
        edgeGeo.setAttribute('position', new THREE.Float32BufferAttribute(edgePositions, 3));
        const edgeMat = new THREE.LineBasicMaterial({ color: 0x0284C7, linewidth: 2 });
        const polyEdges = new THREE.LineSegments(edgeGeo, edgeMat);
        polyGroup.add(polyEdges);

        // Polytope Nodes
        const nodeSpheres = [];

        // Vertices (Obsidian)
        const vertMat = new THREE.MeshStandardMaterial({ color: 0x0F172A, roughness: 0.2, metalness: 0.8 });
        verts.forEach(v => {
            const m = new THREE.Mesh(sphereGeo, vertMat);
            m.position.set(v[0], v[1], v[2]);
            m.scale.set(0.10, 0.10, 0.10);
            m.userData = { type: 'Vertex', coord: v };
            polyGroup.add(m);
            nodeSpheres.push(m);
        });

        // Interior Points (Emerald)
        const intMat = new THREE.MeshStandardMaterial({
            color: 0x10B981,
            emissive: 0x059669,
            emissiveIntensity: 0.55,
            roughness: 0.2
        });
        payload.interiorPoints.forEach(p => {
            const m = new THREE.Mesh(sphereGeo, intMat);
            m.position.set(p[0], p[1], p[2]);
            m.scale.set(0.085, 0.085, 0.085);
            m.userData = { type: 'Interior Point', coord: p };
            polyGroup.add(m);
            nodeSpheres.push(m);
        });

        // Boundary Points
        const bndMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.4 });
        payload.boundaryPoints.forEach(p => {
            const key = `${p[0]},${p[1]},${p[2]}`;
            if (!vertexSet.has(key)) {
                const m = new THREE.Mesh(sphereGeo, bndMat);
                m.position.set(p[0], p[1], p[2]);
                m.scale.set(0.07, 0.07, 0.07);
                m.userData = { type: 'Boundary Point', coord: p };
                polyGroup.add(m);
                nodeSpheres.push(m);
            }
        });

        // Distinguished point p* (Crimson)
        if (payload.pStar) {
            const p = payload.pStar;
            const pMat = new THREE.MeshStandardMaterial({
                color: 0xEF4444,
                emissive: 0xDC2626,
                emissiveIntensity: 0.85,
                roughness: 0.1
            });
            const pMesh = new THREE.Mesh(sphereGeo, pMat);
            pMesh.position.set(p[0], p[1], p[2]);
            pMesh.scale.set(0.12, 0.12, 0.12);
            pMesh.userData = { type: 'Distinguished Point p*', coord: p };
            polyGroup.add(pMesh);
            nodeSpheres.push(pMesh);
        }

        scene.add(polyGroup);

        // 10. Game Flight Keyboard Controls
        const keys = { w: false, a: false, s: false, d: false, q: false, e: false, shift: false };
        window.addEventListener('keydown', (ev) => {
            const k = ev.key.toLowerCase();
            if (k in keys) keys[k] = true;
            if (ev.key === 'Shift') keys.shift = true;
        });
        window.addEventListener('keyup', (ev) => {
            const k = ev.key.toLowerCase();
            if (k in keys) keys[k] = false;
            if (ev.key === 'Shift') keys.shift = false;
        });

        function updateFlight(delta) {
            const speed = (keys.shift ? 12.0 : 4.0) * delta;
            const forward = new THREE.Vector3();
            camera.getWorldDirection(forward);
            forward.z = 0;
            forward.normalize();

            const right = new THREE.Vector3();
            right.crossVectors(forward, camera.up).normalize();

            if (keys.w) {
                camera.position.addScaledVector(forward, speed);
                controls.target.addScaledVector(forward, speed);
            }
            if (keys.s) {
                camera.position.addScaledVector(forward, -speed);
                controls.target.addScaledVector(forward, -speed);
            }
            if (keys.d) {
                camera.position.addScaledVector(right, speed);
                controls.target.addScaledVector(right, speed);
            }
            if (keys.a) {
                camera.position.addScaledVector(right, -speed);
                controls.target.addScaledVector(right, -speed);
            }
            if (keys.e) {
                camera.position.z += speed;
                controls.target.z += speed;
            }
            if (keys.q) {
                camera.position.z -= speed;
                controls.target.z -= speed;
            }
        }

        // 11. Raycasting Inspector
        const raycaster = new THREE.Raycaster();
        const mouse = new THREE.Vector2();

        container.addEventListener('mousemove', (ev) => {
            const rect = container.getBoundingClientRect();
            mouse.x = ((ev.clientX - rect.left) / container.clientWidth) * 2 - 1;
            mouse.y = -((ev.clientY - rect.top) / container.clientHeight) * 2 + 1;

            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(nodeSpheres);

            if (intersects.length > 0) {
                const hit = intersects[0].object.userData;
                inspector.innerHTML = `<span style="color: #38BDF8; font-weight: 700;">${hit.type}:</span> (${hit.coord.join(', ')})`;
            } else {
                inspector.innerHTML = `<span style="color: #94A3B8;">Inspector:</span> Ready`;
            }
        });

        // 12. Toolbar Actions
        let autoSpin = false;
        document.getElementById("__UID___btn_orbit").onclick = () => {
            autoSpin = !autoSpin;
            controls.autoRotate = autoSpin;
            controls.autoRotateSpeed = 2.0;
            document.getElementById("__UID___btn_orbit").style.color = autoSpin ? "#38BDF8" : "#E2E8F0";
        };

        let showGrid = true;
        document.getElementById("__UID___btn_grid").onclick = () => {
            showGrid = !showGrid;
            infiniteGrid.visible = showGrid;
            ambientInstanced.visible = showGrid;
            document.getElementById("__UID___btn_grid").style.color = showGrid ? "#E2E8F0" : "#64748B";
        };

        let showAxes = true;
        document.getElementById("__UID___btn_axes").onclick = () => {
            showAxes = !showAxes;
            axesGroup.visible = showAxes;
            document.getElementById("__UID___btn_axes").style.color = showAxes ? "#E2E8F0" : "#64748B";
        };

        document.getElementById("__UID___btn_reset").onclick = () => {
            camera.position.set(7.5, -8.5, 6.0);
            controls.target.set(0.5, 0.5, 0.8);
            controls.update();
        };

        document.getElementById("__UID___btn_fs").onclick = () => {
            if (!document.fullscreenElement) {
                wrapper.requestFullscreen().catch(err => {});
            } else {
                document.exitFullscreen().catch(err => {});
            }
        };

        // 13. Animation Loop
        let clock = new THREE.Clock();
        function animate() {
            requestAnimationFrame(animate);
            const delta = clock.getDelta();
            updateFlight(delta);
            controls.update();
            renderer.render(scene, camera);
        }
        animate();

        // Responsive Resize
        window.addEventListener('resize', () => {
            const w = container.clientWidth;
            const h = container.clientHeight;
            camera.aspect = w / h;
            camera.updateProjectionMatrix();
            renderer.setSize(w, h);
        });
    }

    init();
})();
</script>
"""


def _json_default(obj: Any) -> Any:
    if hasattr(obj, '__int__'):
        try:
            return int(obj)
        except Exception:
            pass
    if hasattr(obj, '__float__'):
        try:
            return float(obj)
        except Exception:
            pass
    return str(obj)


def generate_threejs_polytope_html(
    vertices: Sequence[Sequence[Any]],
    facets: Sequence[Sequence[int]],
    *,
    interior_points: Sequence[Sequence[Any]] = (),
    boundary_points: Sequence[Sequence[Any]] = (),
    p_star: Optional[Sequence[Any]] = None,
    title: str = "Lattice Polytope P ⊂ ℝ³",
    latex_label: str = "",
    invariants: Optional[Mapping[str, Any]] = None,
    height: int = 580,
    lattice_range: int = 8,
) -> str:
    """
    Generate a self-contained interactive 3D HTML viewer with game controls,
    infinite shader grid, vast ZZ^3 instanced lattice, and glassmorphic polytope mesh.
    """
    uid = f"threejs_polytope_{uuid.uuid4().hex[:8]}"

    data_payload = {
        "vertices": [[float(c) for c in v] for v in vertices],
        "facets": [[int(i) for i in f] for f in facets],
        "interiorPoints": [[float(c) for c in p] for p in interior_points],
        "boundaryPoints": [[float(c) for c in p] for p in boundary_points],
        "pStar": [float(c) for c in p_star] if p_star is not None else None,
        "title": title,
        "latexLabel": latex_label,
        "invariants": {str(k): _json_default(v) for k, v in (invariants or {}).items()},
        "latticeRange": int(lattice_range),
    }
    json_str = json.dumps(data_payload, default=_json_default)

    out = (
        _TEMPLATE
        .replace("__UID__", uid)
        .replace("__HEIGHT__", str(height))
        .replace("__TITLE__", title)
        .replace("__PAYLOAD__", json_str)
    )
    return out
