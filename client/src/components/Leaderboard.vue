<template>
  <div class="main-content" style="height: 100vh;">
    <div class="d-flex flex-column align-items-center logo mt-5">
      <img class="fit-picture" src="../assets/heineken.png"/>
    </div>
    <div v-if="this.status_loading === false">
      <div class="svg-container">
        <svg class="ip" viewBox="0 0 256 128" width="256px" height="128px" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="grad1" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="#5ebd3e" />
              <stop offset="33%" stop-color="#ffb900" />
              <stop offset="67%" stop-color="#f78200" />
              <stop offset="100%" stop-color="#e23838" />
            </linearGradient>
            <linearGradient id="grad2" x1="1" y1="0" x2="0" y2="0">
              <stop offset="0%" stop-color="#e23838" />
              <stop offset="33%" stop-color="#973999" />
              <stop offset="67%" stop-color="#009cdf" />
              <stop offset="100%" stop-color="#5ebd3e" />
            </linearGradient>
          </defs>
          <g fill="none" :stroke-linecap="strokeLinecap" :stroke-width="strokeWidth">
            <g class="ip__track" :stroke="trackStrokeColor">
              <path :d="trackPath" />
              <path :d="reverseTrackPath" />
            </g>
            <g :stroke-dasharray="dashArray">
              <path class="ip__worm1" :stroke="worm1StrokeColor" :stroke-dashoffset="worm1DashOffset" :d="trackPath" />
              <path class="ip__worm2" :stroke="worm2StrokeColor" :stroke-dashoffset="worm2DashOffset" :d="reverseTrackPath" />
            </g>
          </g>
        </svg>
      </div>
      <h2 class="text-center margin-top">Loading...</h2>
    </div>
    <div v-else>
      <h1 class="text-center">Here are our Top 3 Leaderboard!</h1>
      <br><br>
      <div class="row">
        <div v-for="(user, index) in users" :key="index" class="col-sm-4">
          <div :class="['leaderboard-card', {'leaderboard-card--first': index === 1}]">
            <div class="leaderboard-card__top">
              <h3 class="text-center">{{ user.points }}</h3>
            </div>
            <div class="leaderboard-card__body">
              <div class="text-center">
                <img src="../assets/defaultUser.png" class="circle-img mb-2 bg-white" :alt="user.name">
                <h3>{{ user.position }}</h3>
                <h5 class="mb-0">{{ user.name }}</h5>
                <p class="text-muted mt-1 mb-0">@{{ user.ig_username }}</p>
                <hr>
                <div class="d-flex justify-content-center align-items-center flex-column">
                  <span><i class="fa fa-map-marker"></i> {{ user.totalCups }} Cups</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex flex-column align-items-center mt-4">
        <h3 class="text-center user p-2">Nice! You're in P{{ this.position }}<br>with {{ this.points_user }} points!</h3>
      </div>
      <div class="d-flex flex-column align-items-center mt-3">
        <p class="small-print">Returning to home in {{ this.timeLeft }}s</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      status_loading: false,
      position: "0",
      points_user: 0,
      timeLeft: 1000,
      userid: '',
      landingPagePushed: false,
      firstpoints: null,
      firstname: null,
      firstposition: 1,
      firstig_username: null,
      firsttotalCups: 0,
      secondpoints: null,
      secondname: null,
      secondposition: 2,
      secondig_username: null,
      secondtotalCups: 0,
      thirdpoints: null,
      thirdname: null,
      thirdposition: 3,
      thirdig_username: null,
      thirdtotalCups: 0,
      users: []
    };
  },
  created() {
    const resultData = this.$route.params;
    this.userid = resultData.id;
    console.log(`User ID: ${this.userid}`);
    this.getLeaderBoard();
    this.startCountdown();
  },
  methods: {
    updateUsers() {
      this.users = [
        {
          points: this.secondpoints,
          name: this.secondname,
          position: this.secondposition,
          ig_username: this.secondig_username,
          totalCups: this.secondtotalCups
        },
        {
          points: this.firstpoints,
          name: this.firstname,
          position: this.firstposition,
          ig_username: this.firstig_username,
          totalCups: this.firsttotalCups
        },
        {
          points: this.thirdpoints,
          name: this.thirdname,
          position: this.thirdposition,
          ig_username: this.thirdig_username,
          totalCups: this.thirdtotalCups
        }
      ];
    },
    goToLandingPage() {
      if (!this.landingPagePushed) {
        this.landingPagePushed = true;
        this.$router.push('/');
      }
    },
    startCountdown() {
      setInterval(() => {
        if (this.timeLeft > 0) {
          this.timeLeft--;
        } else {
          this.goToLandingPage();
        }
      }, 1000);
    },
    updateLeaderBoard() {
      this.getTop3()
        .then((response) => {
          const data = response.data;
          const firstUser = data.first;
          if (typeof firstUser.final_point !== 'undefined') {
            this.firstpoints = firstUser.final_point;
          } else {
            this.firstpoints = 0;
          }
          this.firstname = firstUser.FirstName;
          this.firstig_username = firstUser.Username;
          if (typeof firstUser.cups !== 'undefined') {
            this.firsttotalCups = firstUser.cups;
          } else {
            this.firsttotalCups = 0;
          }
          const secondUser = data.second;
          this.secondpoints = secondUser.final_point;
          if (typeof secondUser.final_point !== 'undefined') {
            this.secondpoints = secondUser.final_point;
          } else {
            this.secondpoints = 0;
          }
          this.secondname = secondUser.FirstName;
          this.secondig_username = secondUser.Username;
          if (typeof secondUser.cups !== 'undefined') {
            this.secondtotalCups = secondUser.cups;
          } else {
            this.secondtotalCups = 0;
          }
          const thirdUser = data.third;
          if (typeof thirdUser.final_point !== 'undefined') {
            this.thirdpoints = thirdUser.final_point;
          } else {
            this.thirdpoints = 0;
          }
          this.thirdname = thirdUser.FirstName;
          this.thirdig_username = thirdUser.Username;
          if (typeof thirdUser.cups !== 'undefined') {
            this.thirdtotalCups = thirdUser.cups;
          } else {
            this.thirdtotalCups = 0;
          }
          console.log(firstUser)
          console.log(secondUser)
          this.updateUsers();
          console.log(thirdUser)
        })
        .catch((error) => {
          console.log(error);
        })
    },
    async getLeaderBoard() {
      console.log("Bonus Point Ran");
      await this.getUsersPoints();
      setTimeout(() => {
        this.getUserPosition();
        this.updateLeaderBoard();
        this.status_loading = true;
      }, 2000);
    },
    getUsersPoints() {
      if (this.userid === null) {
        console.log("Missing userid");
        return Promise.reject("Missing userid");
      }

      const payload = {
        document_id: this.userid,
        read: true
      };
      const path = `https://5000-joashlaw75-techducks-htn4hymsh8o.ws-us97.gitpod.io/${this.userid}/bonus`;

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          console.log("Bonus Point Calculation Finish")
          return response;
        })
        .catch((error) => {
          console.log(error);
          throw error;
        });
    },
    getUserPosition() {
      if (this.userid === null) {
        console.log("Missing userid");
        return Promise.reject("Missing userid");
      }

      const payload = {
        document_id: this.userid,
        read: true
      };
      const path = `https://5000-joashlaw75-techducks-htn4hymsh8o.ws-us97.gitpod.io/leaderboard/${this.userid}`; 

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          this.position = response.data.user_rank;
          this.points_user = response.data.user_point;
          console.log(this.position)
          console.log(this.points_user)
          return response;
        })
        .catch((error) => {
          console.log(error);
          throw error;
        });
    },
    getTop3() {
      const payload = {
        button_id: "top_3",
        read: true
      };
      const path = `https://5000-joashlaw75-techducks-htn4hymsh8o.ws-us97.gitpod.io/leaderboard`;

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
          .then((response) => {
            return response;
          })
          .catch((error) => {
            throw error;
          });
    }
  },
  computed: {
    strokeLinecap() {
      return "round";
    },
    strokeWidth() {
      return "16";
    },
    trackStrokeColor() {
      return "#ddd";
    },
    worm1StrokeColor() {
      return "url(#grad1)";
    },
    worm2StrokeColor() {
      return "url(#grad2)";
    },
    dashArray() {
      return "180 656";
    },
    worm1DashOffset() {
      return "0";
    },
    worm2DashOffset() {
      return "358";
    },
    trackPath() {
      return "M8,64s0-56,60-56,60,112,120,112,60-56,60-56";
    },
    reverseTrackPath() {
      return "M248,64s0-56-60-56-60,112-120,112S8,64,8,64";
    },
  }
};
</script>

<style scoped>

body {
  background: #f9f9f9;
  font-family: "Roboto", sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-content {
  height: 100vh;
  padding: 20px 20px;
  border: 10px;
}

.user {
  width: 400px;
  border-radius: 10px;
  color: white;
  background-color: #038135 !important;
}

.small-print {
  transform: scale(0.75);
  position: fixed;
  margin-bottom: 50px;
  text-align: center !important;
}

.leaderboard-card {
  background: #fff;
  margin-bottom: 40px;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
.leaderboard-card--first {
  transform: scale(1.05);
  margin-bottom: 15px !important;
}

.leaderboard-card.leaderboard-card--first .leaderboard-card__top {
  background: linear-gradient(45deg, #7e57c2, #ab47bc);
  color: #fff;
}
.leaderboard-card__top {
  background: #f9f6ff;
  padding: 20px 0 30px 0;
}
.leaderboard-card__body {
  padding: 15px;
  margin-top: -40px;
}

img.circle-img {
  height: 70px;
  width: 70px;
  border-radius: 70px;
  border: 3px solid #fff;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
img.circle-img.circle-img--small {
  height: 55px;
  width: 55px;
  border-radius: 55px;
}

.table {
  border-spacing: 0 15px;
  border-collapse: separate;
}
.table thead tr th,
.table thead tr td,
.table tbody tr th,
.table tbody tr td {
  vertical-align: middle;
  border: none;
}
.table thead tr th:nth-last-child(1),
.table thead tr td:nth-last-child(1),
.table tbody tr th:nth-last-child(1),
.table tbody tr td:nth-last-child(1) {
  text-align: center;
}
.table tbody tr {
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}
.table tbody tr td {
  background: #fff;
}
.table tbody tr td:nth-child(1) {
  border-radius: 5px 0 0 5px;
}
.table tbody tr td:nth-last-child(1) {
  border-radius: 0 5px 5px 0;
}

.svg-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 150px;
}

* {
  border: 0;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --hue: 223;
  --bg: hsl(var(--hue), 90%, 95%);
  --fg: hsl(var(--hue), 90%, 5%);
  --trans-dur: 0.3s;
  font-size: calc(16px + (24 - 16) * (100vw - 320px) / (1280 - 320));
}

body {
  background-color: var(--bg);
  color: var(--fg);
  font: 1em/1.5 sans-serif;
  height: 100vh;
  display: grid;
  place-items: center;
  transition: background-color var(--trans-dur);
}

main {
  padding: 1.5em 0;
}

.ip {
  width: 16em;
  height: 8em;
}

.ip__track {
  stroke: hsl(var(--hue), 90%, 90%);
  transition: stroke var(--trans-dur);
}

.ip__worm1,
.ip__worm2 {
  animation: worm1 2s linear infinite;
}

.ip__worm2 {
  animation-name: worm2;
}

/* Dark theme */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: hsl(var(--hue), 90%, 5%);
    --fg: hsl(var(--hue), 90%, 95%);
  }

  .ip__track {
    stroke: hsl(var(--hue), 90%, 15%);
  }
}

/* Animation */
@keyframes worm1 {
  from {
    stroke-dashoffset: 0;
  }
  50% {
    animation-timing-function: steps(1);
    stroke-dashoffset: -358;
  }
  50.01% {
    animation-timing-function: linear;
    stroke-dashoffset: 358;
  }
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes worm2 {
  from {
    stroke-dashoffset: 358;
  }
  50% {
    stroke-dashoffset: 0;
  }
  to {
    stroke-dashoffset: -358;
  }
}

.margin-top {
  margin-top: 150px;
  font-size: 3rem;
}
</style>
