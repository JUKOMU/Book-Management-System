/* 粒子动效 */
const canvas = document.getElementById("side-canvas");
const ctx = canvas.getContext("2d");
const width = window.innerWidth;
const height = window.innerHeight;

canvas.width = width;
canvas.height = height;

const particles = [];
const particleCount = 100;
const particleSpeed = 2;
const particleSize = 5;
const colors = ["#E74C3C", "#3498DB", "#2ECC71", "#F1C40F", "#E67E22"];

class Particle {
    constructor() {
        this.x = width / 2;
        this.y = height / 2;
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.angle = Math.random() * 360;
        this.speed = Math.random() * particleSpeed;
    }

    update() {
        this.x += Math.cos(this.angle) * this.speed;
        this.y += Math.sin(this.angle) * this.speed;

        if (this.x < 0 || this.x > width || this.y < 0 || this.y > height) {
            this.x = width / 2;
            this.y = height / 2;
        }
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, particleSize, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
    }
}

function createParticles() {
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
}

function animate() {
    ctx.clearRect(0, 0, width, height);

    for (const particle of particles) {
        particle.update();
        particle.draw();
    }

    requestAnimationFrame(animate);
}

createParticles();
animate();
