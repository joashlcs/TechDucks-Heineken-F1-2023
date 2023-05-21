<template>
  <div class="d-flex flex-wrap justify-content-center align-items-center flex-column col" style="height: 100vh;">

    <div class="logo">
      <img class="fit-picture" src="../assets/heineken.png"/>
    </div>
    <div v-if="result === 'passed'" class="text-center mt-1">
      <div class="m-3 text-center">
        <h2 class="fs-1">Congratulations!</h2>
        <h2 class="fs-1">You're under 0.600s!</h2>
        <img class="gif" src="../assets/congratulation.gif" alt="Looping GIF" loop>
        <h2 class="mx-5">Present your QR code @ the stores for <b>{{ percentageOff }}%</b> off!</h2>
      </div>
      <div class="text-center mt-5">
        <a href="/">
          <p v-if="timeLeft >= 0">Returning to home in {{ timeLeft }} seconds...</p>
        </a>
      </div>
    </div>
    <div v-else class="text-center mt-3">
      <div class="mb-3">
        <h2 class="mt-2">Oh no!</h2>
        <h2>You're <b>over</b> 0.600s.</h2>
        <img class="gif big mt-1" src="../assets/firstbeer_failed.gif" alt="Looping GIF" loop>
        <h2 class="mt-2">Try Again Tomorrow!</h2>
        <p class="mt-3">*Hint: Don't drink before trying this out!*</p>
      </div>
      <div class="text-center mt-5">
        <a href="/">
          <p v-if="timeLeft >= 0">Returning to home in {{ timeLeft }} seconds...</p>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import QRCodeScanner from "@/components/QRCodeScanner.vue";
import axios from "axios";

export default {
  data() {
    return {
      msg: '',
      userid: '',
      result: null,
      timeLeft: 10,
      percentageOff: 10,
      landingPagePushed: false,
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
    // Start the countdown timer
    this.getPercentageOff()
      .then((response) => {
        const data = response.data;
        this.percentageOff = data.discount_percentage;
        console.log(this.percentageOff)
      })
      .catch((error) => {
        console.log(error);
      })
    this.startCountdown();
  },
  methods: {
    updateCupCount() {
      if (this.userid === '') {
        console.log("Missing document_id");
        return Promise.reject("Missing document_id");
      }

      const payload_landing = {
        document_id: this.userid,
        read: true
      };
      const path = `http://127.0.0.1:5000/${this.userid}/cup-update`;

      return axios.post(path, payload_landing, {
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
    goToLandingPage() {
      if (!this.landingPagePushed) {
        this.landingPagePushed = true; // Set the flag to indicate that landing page has been pushed
        this.$router.push('/');
      }
    },
    startCountdown() {
      setInterval(() => {
        if (this.timeLeft > 0) {
          this.timeLeft--;
        } else {
          if (this.result === 'passed') {
            if (!this.landingPagePushed) {
              console.log("Updating Cup Count by 1");
              this.updateCupCount(); // Call updateCupCount only when result is "passed"
            }
          }
          this.goToLandingPage();
        }
      }, 1000);
    },
    getPercentageOff() {
      if (this.userid === '') {
        console.log("Missing document_id");
        return Promise.reject("Missing document_id");
      }

      const payload_landing = {
        document_id: this.userid,
        read: true
      };
      const path = `http://127.0.0.1:5000/${this.userid}/discount`;

      return axios.post(path, payload_landing, {
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
    }
  },
};
</script>


<style scoped>
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
