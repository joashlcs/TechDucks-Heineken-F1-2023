<template>
  <div class="d-flex flex-wrap justify-content-center align-items-center flex-column" style="height: 100vh;">
    <div class='double'>
      <template v-if="type === 'cashless'">
        <div class="logo">
          <img class="fit-picture" src="../assets/heineken.png"/>
        </div>
        <PaymentQRDetector></PaymentQRDetector>
        <div class="text-center mt-3">
          <img class="fit-picture-2" src="../assets/payment.png"/>
        </div>
        <div class="mt-5 text-center">
          <span class="btn-heineken background-heineken-green">Make your payment below!</span>
        </div>
        <img class="mt-5 scroll-down-link scroll-down-arrow" src="../assets/down-arrow-double.png"/>
      </template>
      <template v-else>
        <div class="logo">
          <img class="fit-picture" src="../assets/heineken.png"/>
        </div>
        <div class="text-center mt-3">
          <img class="fit-picture-2" src="../assets/heineken-shop.png"/>
        </div>
        <div class="mt-5 text-center">
          <span class="btn-heineken background-heineken-green">Show your QR code & make payment!</span>
          <p class="mt-4">@ the heineken store</p>
        </div>
        <img class="mt-3-heineken slide-right img-2" src="../assets/right-arrow-double.png"/>
      </template>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PaymentQRDetector from "@/components/PaymentQRDetector.vue";

export default {
  data() {
    return {
      msg: '',
      userid: '',
      type: '',
    };
  },
  components: {
    PaymentQRDetector
  },
  created() {
      const resultData = this.$route.params;
      this.userid = resultData.id;
      this.type = resultData.type;
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
  }
};
</script>

<style scoped>
.double {
  transform: scale(1.3);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.img-2 {
  width: 50px;
}

h1 {
  line-height: 1 !important;
}
span {
  font-size: large !important;
}
.fit-picture {
  width: 250px;
}

.fit-picture-2 {
  width: 200px;
}

.btn-heineken {
  color: white !important;
  border-radius: 10px !important;
  padding: 15px;
}

.background-heineken-green {
  background-color: #038135 !important;
  color: white !important;
}

.heineken-text-glow {
  color: #FFD501;
  text-shadow: 4px 4px 3px rgba(255, 213, 1, 0.9);
}

.slide-right {
  animation: slide-right 1.3s cubic-bezier(0.250, 0.460, 0.450, 0.940) both infinite;
}

.scroll-down-arrow {
  background-size: contain;
  background-repeat: no-repeat;
}

.scroll-down-link {
  display: flex;
  justify-content: center;
  position: relative;
  z-index: 100;
  cursor: pointer;
  height: 60px;
  width: 80px;
  margin-top: 20px;
  margin-left: auto;
  margin-right: auto;
  line-height: 60px;
  left: 0%;
  bottom: 10px;
  color: #FFF;
  text-align: center;
  font-size: 70px;
  text-decoration: none;
  text-shadow: 0px 0px 3px rgba(0, 0, 0, 0.4);
  -webkit-animation: fade_move_down 2s ease-in-out infinite;
}

@-webkit-keyframes fade_move_down {
  0% { -webkit-transform: translate(0, -20px); opacity: 0; }
  50% { opacity: 1; }
  100% { -webkit-transform: translate(0, 0px); opacity: 0; }
}

@keyframes slide-right {
  0% {
    -webkit-transform: translateX(-50px);
            transform: translateX(-50px);
  }
  100% {
    -webkit-transform: translateX(50px);
            transform: translateX(50px);
  }
}

.mt-3-heineken {
  display: flex;
  justify-content: center;
  position: relative;
  z-index: 100;
  cursor: pointer;
  width: 50px;
  margin-top: 40px;
  margin-left: auto;
  margin-right: auto;
  line-height: 60px;
  left: 0%;
  bottom: 10px;
}

</style>
