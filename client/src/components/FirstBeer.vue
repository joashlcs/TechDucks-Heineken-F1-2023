<template>
  <div class="d-flex flex-wrap justify-content-center align-items-center flex-column col" style="height: 100vh;">
    <div class="logo">
      <img class="fit-picture" src="../assets/heineken.png"/>
    </div>
    <div v-if="result === 'passed'" class="text-center mt-1">
      <img class="gif" src="../assets/congratulation.gif" alt="Looping GIF" loop>
      <div class="m-4 text-center">
        <h2>Congratulations! You're under 0.600s!</h2>
        <h2>Present your QR code @ the stores for <b>{{ percentageOff }}%</b> off!</h2>
      </div>
    </div>
    <div v-else class="text-center ">
      <img class="gif big" src="../assets/firstbeer_failed.gif" alt="Looping GIF" loop>
      <div>
        <h2>Oh no! You're over 0.600s.</h2>
        <h2>Try Again Tomorrow!</h2>
      </div>
    </div>
    <div class="text-center mt-3">
      <a href="/">
        <p v-if="timeLeft >= 0">Returning to home in {{ timeLeft }} seconds...</p>
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import QRCodeScanner from "@/components/QRCodeScanner.vue";

export default {
  name: 'LandingPage',
  data() {
    return {
      msg: '',
      userid: null,
      result: null,
      timeLeft: 10,
      percentageOff: 10,
    };
  },
  components: {
    QRCodeScanner
  },
  created() {
    const resultData = this.$route.params;
    this.userid = resultData.id;
    this.result = resultData.result;
    console.log(`User ID: ${this.userid}`);
    console.log(`User ID: ${this.result}`);
    this.startCountdown(); // Start the countdown timer
    this.getPercentageOff();
  },
  methods: {
    getMessage() {
      // Your existing code here
    },
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
    getPercentageOff() {
      // Call An API to discount using discount chart.
    }
  },
};
</script>

<style>
h1 {
  line-height: 1 !important;
}

a {
  color: inherit !important;
  text-decoration: none !important;
}

.gif {
  max-width: 300px;
  max-height: 300px;
}

.gif big{
  max-width: 400px;
  max-height: 400px;
}

.fit-picture {
  width: 250px;
}
</style>
