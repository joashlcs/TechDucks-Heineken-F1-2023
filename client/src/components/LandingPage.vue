<template>
  <QRCodeScanner></QRCodeScanner>
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
    <div class="mt-5 text-center">
      <span class="btn-heineken background-heineken-green">Scan Your QR Code Below</span>
    </div>
    <img class="scroll-down-link scroll-down-arrow" src="../assets/down-arrow.png"/>
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
    };
  },
  components: {
    QRCodeScanner
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
    created() {
      this.getMessage();
    },
  }
};
</script>

<style>
h1 {
  line-height: 1 !important;
}
span {
  font-size: large !important;
}
.fit-picture {
  width: 250px;
}
.btn-heineken {
  transform: scale(1.75);
  color: white !important;
  border-radius: 10px !important;
  padding: 10px;
}

.background-heineken-green {
  background-color: #038135 !important;
  color: white !important;
}

.heineken-text-glow {
  color: #FFD501;
  text-shadow: 4px 4px 3px rgba(255, 213, 1, 0.9);
}

.scroll-down-arrow {
  background-size: contain;
  background-repeat: no-repeat;
}

.scroll-down-link {
  position: relative;
  z-index: 100;
  cursor: pointer;
  height: 60px;
  width: 80px;
  margin: 20px 0 0 0px;
  line-height: 60px;
  left: 0%;
  bottom: 10px;
  color: #FFF;
  text-align: center;
  font-size: 70px;
  text-decoration: none;
  text-shadow: 0px 0px 3px rgba(0, 0, 0, 0.4);
  -webkit-animation: fade_move_down 2s ease-in-out infinite;
  -moz-animation: fade_move_down 2s ease-in-out infinite;
  animation: fade_move_down 2s ease-in-out infinite;
}

@-webkit-keyframes fade_move_down {
  0% { -webkit-transform: translate(0, 0px); opacity: 0; }
  50% { opacity: 1; }
  100% { -webkit-transform: translate(0, 20px); opacity: 0; }
}

@-moz-keyframes fade_move_down {
  0% { -moz-transform: translate(0, 0px); opacity: 0; }
  50% { opacity: 1; }
  100% { -moz-transform: translate(0, 20px); opacity: 0; }
}

@keyframes fade_move_down {
  0% { transform: translate(0, 0px); opacity: 0; }
  50% { opacity: 1; }
  100% { transform: translate(0, 20px); opacity: 0; }
}
</style>
