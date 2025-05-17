const width = 60, height = 40;
const gridElem = document.getElementById('grid');
const pInfectInput = document.getElementById('pInfect');
const pDisplay = document.getElementById('pDisplay');
const tRecoverInput = document.getElementById('tRecover');
let running = false, timer;

gridElem.style.gridTemplateColumns = `repeat(${width}, 10px)`;

let grid = [], timers = [];

function initGrid() {
    grid = Array.from({ length: height }, () => Array(width).fill('S'));
    timers = Array.from({ length: height }, () => Array(width).fill(0));
    gridElem.innerHTML = '';
    for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
        const cell = document.createElement('div');
        cell.className = 'cell S';
        cell.dataset.x = x;
        cell.dataset.y = y;
        cell.onclick = () => toggleInfection(x, y);
        gridElem.appendChild(cell);
    }
    }
}

function updateView() {
    for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
        const idx = y * width + x;
        const cellElem = gridElem.children[idx];
        cellElem.className = 'cell ' + grid[y][x];
    }
    }
}

function toggleInfection(x, y) {
    if (grid[y][x] === 'I') grid[y][x] = 'S';
    else grid[y][x] = 'I';
    timers[y][x] = 0;
    updateView();
}

function step() {
    const pInfect = parseFloat(pInfectInput.value);
    const tRecover = parseInt(tRecoverInput.value);
    const newGrid = grid.map(row => [...row]);
    const newTimers = timers.map(row => [...row]);
    const dirs = [ [-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[-1,1],[1,-1] ];

    for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
        if (grid[y][x] === 'S') {
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx >= 0 && ny >= 0 && nx < width && ny < height && grid[ny][nx] === 'I') {
            if (Math.random() < pInfect) {
                newGrid[y][x] = 'I';
                newTimers[y][x] = 0;
                break;
            }
            }
        }
        } else if (grid[y][x] === 'I') {
        newTimers[y][x]++;
        if (newTimers[y][x] >= tRecover) {
            newGrid[y][x] = 'R';
        }
        }
    }
    }

    grid = newGrid;
    timers = newTimers;
    updateView();
}

document.getElementById('startBtn').onclick = () => {
    running = !running;
    document.getElementById('startBtn').innerText = running ? 'Пауза' : 'Старт';
    if (running) timer = setInterval(step, 200);
    else clearInterval(timer);
};

document.getElementById('stepBtn').onclick = step;
document.getElementById('clearBtn').onclick = () => {
    initGrid();
};

pInfectInput.oninput = () => {
    pDisplay.textContent = pInfectInput.value;
};

initGrid();