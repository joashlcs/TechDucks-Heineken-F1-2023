<template>
  <BeerQRCodeCupScanner></BeerQRCodeCupScanner>
  <div class="d-flex flex-wrap justify-content-center align-items-center flex-column" style="height: 100vh;">
    <div class="scaled-div">
      <div class="logo">
        <img class="fit-picture" src="../assets/heineken.png"/>
      </div>
      <div>
        <img class="mt-3 fit-picture wobble-ver-right" src="../assets/beer.png" loop/>
      </div>
      <div class="mt-4 mb-5 text-center">
        <span class="btn-heineken fs-5">Place your cup in the holder below</span>
      </div>
    </div>
    <img class="scroll-down-link-page scroll-down-arrow" src="../assets/down-arrow.png"/>
  </div>
</template>


<script>
import axios from 'axios';
import BeerQRCodeCupScanner from "@/components/BeerQRCodeCupScanner.vue";

export default {
  name: 'LandingPage',
  data() {
    return {
      msg: '',
    };
  },
  components: {
    BeerQRCodeCupScanner
  },
};
</script>

<style>
.scaled-div {
  display: flex;
  flex-direction: column;
  align-items: center;
  transform: scale(1.15);
  margin-top: -20px;
}


h1 {
  line-height: 1 !important;
}
span {
  font-size: large !important;
}

.logo {
  z-index: 1;
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

.wobble-ver-right {
	-webkit-animation: wobble-ver-right 2s infinite;
  animation: wobble-ver-right 2s infinite;
}

.scroll-down-arrow {
  background-size: contain;
  background-repeat: no-repeat;
}

.scroll-down-link-page {
  position: fixed;
  z-index: 100;
  cursor: pointer;
  height: 60px;
  width: 80px;
  margin: 0 auto;
  line-height: 60px;
  left: 0;
  right: 0;
  bottom: 50px;
  color: #FFF;
  text-align: center !important;
  font-size: 70px;
  text-decoration: none;
  text-shadow: 0px 0px 3px rgba(0, 0, 0, 0.4);
  -webkit-animation: fade_move_down 2s ease-in-out infinite;
}

@-webkit-keyframes fade_move_down {
  0% { -webkit-transform: translate(0, 0px); opacity: 0; }
  50% { opacity: 1; }
  100% { -webkit-transform: translate(0, 20px); opacity: 0; }
}

@-webkit-keyframes wobble-ver-right {
  0%,
  100% {
    -webkit-transform: translateY(0) rotate(0);
            transform: translateY(0) rotate(0);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
  }
  15% {
    -webkit-transform: translateY(-30px) rotate(6deg);
            transform: translateY(-30px) rotate(6deg);
  }
  30% {
    -webkit-transform: translateY(15px) rotate(-6deg);
            transform: translateY(15px) rotate(-6deg);
  }
  45% {
    -webkit-transform: translateY(-15px) rotate(3.6deg);
            transform: translateY(-15px) rotate(3.6deg);
  }
  60% {
    -webkit-transform: translateY(9px) rotate(-2.4deg);
            transform: translateY(9px) rotate(-2.4deg);
  }
  75% {
    -webkit-transform: translateY(-6px) rotate(1.2deg);
            transform: translateY(-6px) rotate(1.2deg);
  }
}

</style>
