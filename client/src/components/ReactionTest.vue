<template>
  <div class="d-flex justify-content-center align-items-center logo">
    <img class="fit-picture" src="../assets/heineken.png"/>
  </div>
  <div v-if="jumpStart" class="d-flex justify-content-center align-items-center multiplier-2">
    <div class="background-heineken-red pop-up-notice">JUMP START!</div>
  </div>
  <div v-else class="container mb-2">
    <div class="light-strips">
      <div v-for="(group, groupIndex) in lightOn" :key="groupIndex" class="light-group">
        <div v-if="groupIndex % 4 === 0" class="background"></div>
        <div v-for="(light, index) in group" :key="index" class="light-circle" :class="{ on: light }"></div>
      </div>
      <div class="light-bar"></div>
    </div>
  </div>
  <div class="d-flex justify-content-center align-items-center flex-column">
    <div class="mb-4">
      <div class="row">
        <div class="col-12 player-info">
          <div>
            <div>Time: {{ timediff }}</div>
            <div>Best Time: {{ bestTime }}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="mb-3">
      <div class="row">
        <div class="col-12">
          <button v-if="!raceStarted" @click="startRace" class="btn btn-heineken background-heineken-green btn-lg m-3">Start Race</button>
          <button v-else @click="finishRace" class="btn btn-heineken background-heineken-red btn-lg m-3">Finish Race</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      lightOn: [[false, false, false, false], [false, false, false, false], [false, false, false, false], [false, false, false, false], [false, false, false, false]],
      raceStarted: false,
      jumpStart: false,
      startTime: null,
      timediff: null,
      bestTime: null,
    };
  },
  methods: {
    startRace() {
      this.jumpStart = false
      this.raceStarted = true;

      setTimeout(() => {
        if (!this.raceStarted) return;
        this.lightOn[0][0] = true;
        this.lightOn[0][1] = true;
        setTimeout(() => {
          if (!this.raceStarted) return;
          this.lightOn[1][0] = true;
          this.lightOn[1][1] = true;
          setTimeout(() => {
            if (!this.raceStarted) return;
            this.lightOn[2][0] = true;
            this.lightOn[2][1] = true;
            setTimeout(() => {
              if (!this.raceStarted) return;
              this.lightOn[3][0] = true;
              this.lightOn[3][1] = true;
              setTimeout(() => {
                if (!this.raceStarted) return;
                this.lightOn[4][0] = true;
                this.lightOn[4][1] = true;
                const randomDelay = Math.floor(Math.random() * (5000 - 1000 + 1)) + 1000;
                setTimeout(() => {
                  if (!this.raceStarted) return;
                  this.lightOn.forEach(subarray => subarray.fill(false));
                  this.startTime = Date.now()
                }, randomDelay);
              }, 1000);
            }, 1000);
          }, 1000);
        }, 1000);
      }, 1000);
    },
    finishRace() {
      if (this.startTime === null) {
        this.jumpStart = true;
        this.raceStarted = false
        this.lightOn.forEach(subarray => subarray.fill(false));
        this.startTime = null;
        this.timediff = null;
      } else {
        const endTime = Date.now();
        const timeDiff = (endTime - this.startTime) / 1000;
        this.timediff = timeDiff
        this.raceStarted = false
        this.startTime = null;
        if (this.bestTime === null || timeDiff < this.bestTime) {
          this.bestTime = timeDiff;
        }
      }
    },
  },
};
</script>

<style>
.container {
  overflow: hidden;
}

.light-bar {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 10px;
  background-color: black;
  z-index: -1;
  width: 300px;
}

.light-strips {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  height: 300px;
}

.light-group {
  display: flex;
  flex-direction: column-reverse;
  margin: 3px;
  padding: 5px;
  border-radius: 10px;
  background-color: #000000;
}

.light-circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin: 5px 0;
  background-color: #222;
  transition: background-color 0.2s;
}

.light-circle.on {
  background-color: #f00;
}

.background {
  position: absolute;
  top: -5px;
  left: -5px;
  width: calc(100% + 10px);
  height: calc(100% + 10px);
  z-index: -1;
}

.btn-heineken {
  transform: scale(1.75);
  font-size: 1rem !important;
}

.pop-up-notice {
  width: 500px;
  border-radius: 20px;
  text-align: center;
  font-size: 5rem;
}

.background-heineken-green {
  background-color: #038135 !important;
  color: white !important;
}

.background-heineken-red {
  background-color: #E30613 !important;
  color: white !important;
}

.multiplier-2 {
  margin: 94px;
}

.player-info {
  font-size: larger;
}
</style>
