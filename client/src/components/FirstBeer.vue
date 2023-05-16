<template>
  <QRCodeScanner></QRCodeScanner>
  <div class="d-flex flex-wrap justify-content-center align-items-center flex-column" style="height: 100vh;">
    <div class="logo">
      <img class="fit-picture" src="../assets/heineken.png"/>
    </div>
    <div class="text-center mt-3">
      <img v-if="result === 'passed'" class="gif" src="../assets/congratulation.gif" alt="Looping GIF" loop>
    </div>
    <div class="m-5 text-center">
      <h2>Congratulations! You're under 0.600s!</h2>
      <h2>Get yourself a discounted beer @ the stores!</h2>
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
  },
  methods: {
    goToLogin() {
      this.$router.push('/login')
    },
    getMessage() {

      const path = 'http://127.0.0.1:5000/ping';
      axios.get(path)
          .then((res) => {
            this.msg = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
    },
  }
};
</script>

<style>
h1 {
  line-height: 1 !important;
}
.gif {
  max-width: 300px;
  max-height: 300px;
}

.fit-picture {
  width: 250px;
}
.btn-heineken {
  transform: scale(1.75);
  background-color: #038135 !important;
  color: white !important;
  border-radius: 10px !important;
  padding: 10px;
}
</style>
