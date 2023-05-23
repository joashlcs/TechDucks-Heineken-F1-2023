<template>
  <div class="main-content" style="height: 100vh;">
    <div class="d-flex flex-column align-items-center logo mt-5">
      <img class="fit-picture" src="../assets/heineken.png"/>
    </div>
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
              <p class="text-muted mt-1 mb-0">{{ user.ig_username }}</p>
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
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      position: "10",
      points_user: 120,
      timeLeft: 10,
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
          this.firstpoints = firstUser.final_point;
          this.firstname = firstUser.FirstName;
          this.firstig_username = firstUser.Username;
          this.firsttotalCups = firstUser.cups;
          const secondUser = data.second;
          this.secondpoints = secondUser.final_point;
          this.secondname = secondUser.FirstName;
          this.secondig_username = secondUser.Username;
          this.secondtotalCups = secondUser.cups;
          const thirdUser = data.third;
          this.thirdpoints = thirdUser.final_point;
          this.thirdname = thirdUser.FirstName;
          this.thirdig_username = thirdUser.Username;
          this.thirdtotalCups = thirdUser.cups;
          console.log(firstUser)
          console.log(this.users)
          this.updateUsers();
          console.log(thirdUser)
        })
        .catch((error) => {
          console.log(error);
        })
    },
    getLeaderBoard() {
      this.getUsersPoints()
      this.getUserPosition()
      this.updateLeaderBoard()
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
          this.points_user = response.data.message;
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
      const path = `https://5000-joashlaw75-techducks-htn4hymsh8o.ws-us97.gitpod.io/leaderboard/${this.userid}`; // Call API to update final buying decision of drinkaid after consecutive failing

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          this.position = response.data.user_rank;
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
</style>
