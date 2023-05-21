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
      <h3 class="text-center user p-2">Nice Try! You came in {{ this.position }}!</h3>
    </div>
    <div class="d-flex flex-column align-items-center mt-3">
      <p class="small-print">Returning to home in {{ this.timeLeft }}s</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      position: "10th",
      timeLeft: 100,
      users: [
        {
          points: "1,051",
          name: "Sandeep Sandy",
          position: "2nd",
          ig_username: "@sandeep",
          totalCups: 13
        },
        {
          points: "1,254",
          name: "Kiran Acharya",
          position: "1st",
          ig_username: "@kiranacharyaa",
          totalCups: 15
        },
        {
          points: "1,012",
          name: "John doe",
          position: "3rd",
          ig_username: "@johndoe",
          totalCups: 10
        }
      ]
    };
  },
  created() {
    const resultData = this.$route.params;
    console.log(`User ID: ${this.userid}`);
    this.getLeaderBoard();
    this.startCountdown(); // Start the countdown timer

  },
  methods: {
    goToLandingPage() {
      this.$router.push('/');
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
    getLeaderBoard() {

    }
  }
};
</script>

<style scoped>

body {
  background: #f9f9f9;
  font-family: "Roboto", sans-serif;
  display: flex;
  justify-content: center; /* Horizontally center the content */
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
