<template>
    <div class="gobang">
        <canvas id="gobang" width="800" height="600"></canvas>
    </div>
</template>

<script>
const CheckStrWhite = "11111";
const CheckStrBlack = "22222";
export default {
    name: "Gobang",
    data() {
        return {
            ctx: null,
            winGame: false,
            whiteTurn: false, // 白棋轮；true-黑棋轮
            resultArr: [] // 记录棋子位置的数组
        };
    },
    mounted() {
        let _this = this;
        let container = document.getElementById("gobang");

        container.addEventListener("click", _this.handleClick);

        _this.ctx = container.getContext("2d");
        _this.ctx.translate(70, 70);
        _this.drawCheckerboard();
    },
    computed: {
        chessText() {
            return this.whiteTurn ? '白棋' : '黑棋';
        }
    },
    methods: {
        drawCheckerboard() {
            // 画棋盘
            let _this = this;
            _this.ctx.beginPath();
            _this.ctx.fillStyle = "#fff";
            _this.ctx.rect(0, 0, 450, 450);
            _this.ctx.fill();
            for (let i = 0; i < 15; i++) {
                _this.ctx.beginPath();
                _this.ctx.strokeStyle = "#D6D1D1";
                _this.ctx.moveTo(15 + i * 30, 15); //垂直方向画15根线，相距30px;
                _this.ctx.lineTo(15 + i * 30, 435);
                _this.ctx.stroke();
                _this.ctx.moveTo(15, 15 + i * 30); //水平方向画15根线，相距30px;棋盘为14*14；
                _this.ctx.lineTo(435, 15 + i * 30);
                _this.ctx.stroke();

                _this.resultArr.push(new Array(15).fill(0));
            }
            _this.drawText();
        },
        drawChess(x, y) {
            let _this = this;
            let xLine = Math.round((x - 15) / 30); // 竖线第x条
            let yLine = Math.round((y - 15) / 30); // 横线第y条
            if (_this.resultArr[xLine][yLine] !== 0) {
                return;
            }
            let grd = _this.ctx.createRadialGradient(
                xLine * 30 + 15,
                yLine * 30 + 15,
                4,
                xLine * 30 + 15,
                yLine * 30 + 15,
                10
            );
            grd.addColorStop(0, _this.whiteTurn ? "#fff" : "#4c4c4c");
            grd.addColorStop(1, _this.whiteTurn ? "#dadada" : "#000");
            _this.ctx.beginPath();
            _this.ctx.fillStyle = grd;
            _this.ctx.arc(
                xLine * 30 + 15,
                yLine * 30 + 15,
                10,
                0,
                2 * Math.PI,
                false
            );
            _this.ctx.fill();
            _this.ctx.closePath();

            _this.setResultArr(xLine, yLine);
            _this.checkResult(xLine, yLine);
        },
        setResultArr(m, n) {
            let _this = this;
            _this.resultArr[m][n] = _this.whiteTurn ? 1 : 2; // 白棋为1；黑棋为2

        },

        checkResult(m, n) { // 判断是否有5子相连
            let _this = this;
            let checkStr = _this.whiteTurn ? CheckStrWhite : CheckStrBlack;
            // 取出[m,n]横竖斜四条线的一维数组
            let lineVertical = _this.resultArr[m].join('');
            if (lineVertical.indexOf(checkStr) > -1) {
                _this.winGame = true;
                return;
            }
            let lineHorizontal = [];
            for (let i = 0; i < 15; i++) {
                lineHorizontal.push(_this.resultArr[i][n]);
            }
            lineHorizontal = lineHorizontal.join('');
            if (lineHorizontal.indexOf(checkStr) > -1) {
                _this.winGame = true;
                return;
            }
            let line135 = [];
            for (let j = 0; j < 15; j++) {
                if (m - j >= 0 && n - j >= 0) { // 左上角
                    line135.unshift(_this.resultArr[m - j][n - j]);
                }
                if (j > 0 && m + j < 15 && n + j < 15) { // 右下角
                    line135.push(_this.resultArr[m + j][n + j]);
                }
            }
            line135 = line135.join('');
            if (line135.indexOf(checkStr) > -1) {
                _this.winGame = true;
                return;
            }
            let line45 = [];
            for (let j = 0; j < 15; j++) {
                if (m + j < 15 && n - j >= 0) { // 右上角
                    line45.unshift(_this.resultArr[m + j][n - j]);
                }
                if (j > 0 && m - j >= 0 && n + j < 15) { // 左下角
                    line45.push(_this.resultArr[m - j][n + j]);
                }
            }
            line45 = line45.join('');
            if (line45.indexOf(checkStr) > -1) {
                _this.winGame = true;

            }
        },
        drawText() {
            let _this = this;
            _this.ctx.clearRect(435 + 60, 0, 100, 70);
            _this.ctx.fillStyle = "#fff";
            _this.ctx.font = "20px Arial";
            _this.ctx.fillText('本轮：' + _this.chessText, 435 + 70, 35);
        },
        drawResult() {
            let _this = this;
            _this.ctx.fillStyle = "#ff2424";
            _this.ctx.font = "20px Arial";
            _this.ctx.fillText(_this.chessText + '胜！', 435 + 70, 70);
        },
        handleClick(event) {
            let x = event.offsetX - 70;
            let y = event.offsetY - 70;
            if (x < 15 || x > 435 || y < 15 || y > 435) {
                // 点出界的
                return;
            }
            this.drawChess(x, y);
            if (this.winGame) {
                this.drawResult();
                return;
            }
            this.whiteTurn = !this.whiteTurn;
            this.drawText();
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.gobang {
  #gobang {
    background: #2a4546;
  }
}
</style>