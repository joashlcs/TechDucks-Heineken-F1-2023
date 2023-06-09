<template>
  <div class="mt-5">
    <div class="d-flex justify-content-center text-center align-items-center logo">
      <img class="fit-picture" src="../assets/heineken.png" alt="logo"/>
    </div>
    <div class="d-flex flex-column align-items-center col">
      <p class="text-center mx-5 fs-5">Tap click when you're ready to race, then tap again when the lights go out.</p>
      <p class="mb-0 fs-4">Attempts Left: <b>{{ 3 - retryCounter }}</b></p>
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
          <div class="text-center col-12 player-info fs-4">
            <div>Time: {{ timediff }}s</div>
            <div>Best Time: {{ bestTime }}s</div>
          </div>
        </div>
      </div>
      <div class="mb-3">
        <div class="row">
          <div class="col-12">
            <button id="button" :disabled="retryCounter >= 3" v-if="!raceStarted" @click="startRace" class="btn btn-heineken background-heineken-green btn-lg m-3">Start Race</button>
            <button id="button" v-else @click="finishRace" class="btn btn-heineken background-heineken-red btn-lg m-3">Finish Race</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      lightOn: [[false, false, false, false], [false, false, false, false], [false, false, false, false], [false, false, false, false], [false, false, false, false]],
      raceStarted: false,
      jumpStart: false,
      startTime: null,
      timediff: "0.000",
      bestTime: "0.000",
      retryCounter: 0,
      userid: null,
      status: null,
    };
  },
  created() {
    const resultData = this.$route.params;
    this.userid = resultData.id;
    this.status = resultData.status;
    console.log(`User ID: ${resultData}`);
  },
  methods: {
    bestReactionTime() {
      console.log(this.userid)
      if (this.user_id === null) {
        console.log("Missing document_id");
        return Promise.reject("Missing document_id");
      }

      const payload = {
        time: parseFloat(this.bestTime),
        document_id: this.userid,
        read: true
      };
      const path = `https://techducks-api-app-drhnv.ondigitalocean.app/${this.userid}/reaction-time`;
      console.log(path)

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          return response;
        })
        .catch((error) => {
          console.log(error);
          throw error; // Re-throw the error to be caught by the caller
        });
    },
    startRace() {
      this.timediff = "0.000";
      this.jumpStart = false;
      this.raceStarted = true;

      this.retryCounter += 1;
      console.log(this.retryCounter)

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
      let status;
      if (this.startTime === null) {
        this.jumpStart = true;
        this.raceStarted = false
        this.lightOn.forEach(subarray => subarray.fill(false));
        this.startTime = null;
        this.timediff = "0.000";
      } else {
        const endTime = Date.now();
        const timeDiff = (endTime - this.startTime) / 1000;
        this.timediff = timeDiff
        this.raceStarted = false
        this.startTime = null;
        if (this.bestTime === "0.000" || this.timediff < this.bestTime) {
          this.bestTime = timeDiff;
        }
      }
      if (this.retryCounter === 3) {
        this.bestReactionTime()
            .then((response) => {
              console.log(`Response Data: ${response.data.status}`)})
        if (this.bestTime <= 0.6 && this.bestTime !== "0.000") {
          status = "passed";
          this.$router.push(`/${this.status}/${this.userid}/${status}`);
        }
        else {
          status = "failed";
          this.$router.push(`/${this.status}/${this.userid}/${status}`);
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
  width: 350px;
  border-radius: 20px;
  text-align: center;
  font-size: 3rem;
  margin-bottom: 48px;
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
  margin-top: 94px;
  margin-bottom: 94px;
}

.player-info {
  font-size: larger;
}
</style>
