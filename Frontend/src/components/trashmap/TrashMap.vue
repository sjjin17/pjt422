<template>
  <div ref="outerDiv" style="position: relative">
    <canvas
      ref="canvas"
      @mousedown="mousedown"
      @mousemove.prevent="mousemove"
      @wheel.prevent="wheel"
    ></canvas>
    <i
      ref="tooltip"
      style="position: absolute"
      :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }"
    ></i>
  </div>
</template>

<script>
import { Tooltip } from "bootstrap";
export default {
  name: "TrashMap",
  props: ["floor", "width", "height"],
  data() {
    return {
      zoom: 1,
      offsetX: 0,
      offsetY: 0,
      mousePrevX: 0,
      mousePrevY: 0,
      tooltipTop: 0,
      tooltipLeft: 0,
    };
  },
  watch: {
    floor: {
      handler() {
        this.calcAndApplyBaseValues();
        this.loadMapAndDraw();
      },
      deep: true,
    },
    width() {
      this.canvas.width = this.width;
      this.canvas.height = this.height;
      this.calcAndApplyBaseValues();
      this.draw();
    },
    "$store.state.hoveredTrashbin"() {
      this.draw();
      if (this.$store.state.hoveredTrashbin) {
        if (this.tooltip) {
          this.tooltip.dispose();
          this.tooltip = null;
        }

        this.tooltip = new Tooltip(this.$refs.tooltip, {
          placement: "top",
          html: true,
          title: `<b>${
            this.$store.state.hoveredTrashbin.name
          }</b><br />${Math.round(
            this.$store.state.hoveredTrashbin.amount * 100
          )}%`,
          trigger: "manual",
        });

        this.tooltipLeft =
          (this.$store.state.hoveredTrashbin.x + this.offsetX) * this.zoom;
        this.tooltipTop =
          (this.$store.state.hoveredTrashbin.y + this.offsetY - 10) * this.zoom;
        this.tooltip.title = "huh";
        this.tooltip.update();
        this.tooltip.show();
      } else {
        this.tooltip.dispose();
        this.tooltip = null;
      }
    },
    "$store.state.selectedTrashbin"() {
      this.draw();
    },
  },
  methods: {
    draw() {
      this.ctx.resetTransform();
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      this.ctx.scale(this.zoom, this.zoom);
      this.ctx.translate(this.offsetX, this.offsetY);

      this.ctx.drawImage(this.img, 0, 0);

      for (let trashbin of this.floor.trashbins) {
        this.ctx.save();
        this.ctx.fillStyle = trashbin.color;
        this.ctx.fillRect(
          trashbin.x - this.floor.trashbinSize / 2,
          trashbin.y - this.floor.trashbinSize / 2,
          this.floor.trashbinSize,
          this.floor.trashbinSize
        );

        this.ctx.lineWidth = 1;
        this.ctx.strokeStyle = "#000000";
        if (this.$store.state.hoveredTrashbin === trashbin) {
          this.ctx.lineWidth = 2;
          this.ctx.strokeStyle = "#000000";
        }
        if (this.$store.state.selectedTrashbin === trashbin) {
          this.ctx.lineWidth = 2;
          this.ctx.strokeStyle = "#CF2222";
        }
        this.ctx.strokeRect(
          trashbin.x - this.floor.trashbinSize / 2,
          trashbin.y - this.floor.trashbinSize / 2,
          this.floor.trashbinSize,
          this.floor.trashbinSize
        );
        this.ctx.restore();
      }

      for (let trashbin of this.floor.trashbins) {
        this.ctx.save();
        if (trashbin?.hasNotification) {
          this.ctx.fillStyle = "#E54444";
          this.ctx.beginPath();
          this.ctx.arc(
            trashbin.x,
            trashbin.y - this.floor.trashbinSize,
            8,
            0,
            2 * Math.PI
          );
          this.ctx.fill();

          this.ctx.fillStyle = "#000000";
          this.ctx.font = "bold 14px sans-serif";
          this.ctx.textAlign = "center";
          this.ctx.textBaseline = "middle";
          this.ctx.fillText(
            "!",
            trashbin.x,
            trashbin.y - this.floor.trashbinSize
          );
          this.ctx.restore();
        }
      }
    },
    loadMapAndDraw() {
      this.img = new Image();
      this.img.onload = () => {
        this.draw();
      };
      this.img.src = this.floor.src;
    },
    calcAndApplyBaseValues() {
      this.baseZoom = Math.min(
        1,
        this.canvas.width / this.floor.width,
        this.canvas.height / this.floor.height
      );
      this.baseOffsetX = Math.max(
        0,
        (this.canvas.width / this.baseZoom - this.floor.width) / 2
      );
      this.baseOffsetY = Math.max(
        0,
        (this.canvas.height / this.baseZoom - this.floor.height) / 2
      );

      this.zoom = this.baseZoom;
      this.offsetX = this.baseOffsetX;
      this.offsetY = this.baseOffsetY;
    },
    changeZoom(zoomRatio) {
      if (this.zoom * zoomRatio < this.baseZoom * 0.75) {
        this.zoom = this.baseZoom * 0.75;
      } else if (this.zoom * zoomRatio > this.baseZoom * 4) {
        this.zoom = this.baseZoom * 4;
      } else {
        this.zoom *= zoomRatio;
      }
    },
    changeOffset(offsetXDelta, offsetYDelta) {
      this.offsetX += offsetXDelta;
      this.offsetY += offsetYDelta;
    },
    mousedown(ev) {
      if ((ev.buttons & 1) === 0) return;
      ev.stopPropagation();

      this.mousePrevX = ev.offsetX;
      this.mousePrevY = ev.offsetY;

      const canvasX = -this.offsetX + ev.offsetX / this.zoom;
      const canvasY = -this.offsetY + ev.offsetY / this.zoom;

      for (let trashbin of this.floor.trashbins.slice().reverse()) {
        const left = trashbin.x - this.floor.trashbinSize / 2;
        const right = trashbin.x + this.floor.trashbinSize / 2;
        const top = trashbin.y - this.floor.trashbinSize / 2;
        const bottom = trashbin.y + this.floor.trashbinSize / 2;

        if (
          canvasX > left &&
          canvasX < right &&
          canvasY > top &&
          canvasY < bottom
        ) {
          this.$store.dispatch("setSelectedTrashbin", trashbin);
          return;
        }
      }
      this.$store.dispatch("setSelectedTrashbin", null);
    },
    mousemove(ev) {
      if ((ev.buttons & 1) === 1) {
        this.changeOffset(
          (ev.offsetX - this.mousePrevX) / this.zoom,
          (ev.offsetY - this.mousePrevY) / this.zoom
        );
        this.mousePrevX = ev.offsetX;
        this.mousePrevY = ev.offsetY;
        this.draw();
      }

      const canvasX = -this.offsetX + ev.offsetX / this.zoom;
      const canvasY = -this.offsetY + ev.offsetY / this.zoom;

      for (let trashbin of this.floor.trashbins.slice().reverse()) {
        const left = trashbin.x - this.floor.trashbinSize / 2;
        const right = trashbin.x + this.floor.trashbinSize / 2;
        const top = trashbin.y - this.floor.trashbinSize / 2;
        const bottom = trashbin.y + this.floor.trashbinSize / 2;

        if (
          canvasX > left &&
          canvasX < right &&
          canvasY > top &&
          canvasY < bottom
        ) {
          this.$store.dispatch("setHoveredTrashbin", trashbin);
          return;
        }
      }
      this.$store.dispatch("setHoveredTrashbin", null);
    },
    wheel(ev) {
      const prevZoom = this.zoom;
      if (ev.deltaY < 0) this.changeZoom(1.1);
      else if (ev.deltaY > 0) this.changeZoom(1 / 1.1);
      this.changeOffset(
        ev.offsetX / this.zoom - ev.offsetX / prevZoom,
        ev.offsetY / this.zoom - ev.offsetY / prevZoom
      );
      this.draw();
    },
  },
  mounted() {
    this.canvas = this.$refs.canvas;
    this.canvas.width = this.width;
    this.canvas.height = this.height;
    this.ctx = this.canvas.getContext("2d");
    this.calcAndApplyBaseValues();
    this.loadMapAndDraw();
    this.tooltip = null;
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid;
}
</style>
