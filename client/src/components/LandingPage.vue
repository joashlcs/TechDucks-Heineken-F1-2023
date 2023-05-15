<template>
  <div class="d-flex flex-wrap justify-content-center align-items-center flex-column" style="height: 100vh;">
    <div class="logo">
      <img class="fit-picture" src="../assets/heineken.png"/>
    </div>
    <div class="text-center mt-3">
      <h1 class="heineken-text-glow" style="font-size: 5em;">EARN</h1>
      <h1 class="heineken-text-glow" style="font-size: 5em;">YOUR</h1>
      <h1 class="heineken-text-glow" style="font-size: 5em;">FREE</h1>
      <h1 class="heineken-text-glow" style="font-size: 5em;">BEER</h1>
    </div>
    <div class="container mt-5 text-center">
      <button type="button" class="btn btn-heineken btn-lg" @click="goToLogin">Start Now!</button>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'LandingPage',
  data() {
    return {
      msg: '',
    };
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
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style>
h1 {
  line-height: 1 !important;
}
.fit-picture {
  width: 250px;
}
.btn-heineken {
  transform: scale(1.75);
  font-size: 1rem !important;
  background-color: #038135 !important;
  color: white !important;
}
.heineken-text-glow {
  color: #FFD501;
  text-shadow: 4px 4px 3px rgba(255, 213, 1, 0.9);
}
</style>
