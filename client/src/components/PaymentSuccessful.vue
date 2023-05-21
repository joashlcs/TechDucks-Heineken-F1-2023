<template>
  <div class="d-flex flex-wrap justify-content-center align-items-center flex-column" style="height: 100vh;">
    <div class="bigger">
      <div class="logo">
        <img class="fit-picture" src="../assets/heineken.png"/>
      </div>
      <div class="text-center mt-3">
        <div class="container">
          <div class="dummy-positioning d-flex">
            <div class="success-icon">
              <div class="success-icon__tip"></div>
              <div class="success-icon__long"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="mt-5 text-center">
        <h2>Payment Successful!</h2>
      </div>
    </div>
  </div>
</template>


<script>

export default {
  data() {
    return {
      msg: '',
      userid: '',
      countdown: 1,
      landingPagePushed: false,
    };
  },
  methods: {
    startCountdown() {
      setInterval(() => {
        if (this.countdown > 0) {
          this.countdown--;
        } else {
          if (!this.landingPagePushed) {
            this.landingPagePushed = true;
            this.$router.push(`/leaderboard/${this.userid}`);
          }
        }
      }, 1000);
    },
  },
  created() {
      const resultData = this.$route.params;
      this.userid = resultData.id;
      this.startCountdown();
  },
};
</script>

<style scoped>
h1 {
  line-height: 1 !important;
}
span {
  font-size: large !important;
}

.bigger {
  transform: scale(1.3);
}

.fit-picture {
  width: 250px;
}

.container {
  width: 250px;
  height: 250px;
}

.dummy-positioning {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.success-icon {
  display: inline-block;
  width: 8em;
  height: 8em;
  font-size: 20px; /* Replace with your preferred size value */
  border-radius: 50%;
  border: 6px solid #6fd443; /* Increased border width and specific color value */
  background-color: #fff;
  position: relative;
  overflow: hidden;
  transform-origin: center;
  animation: showSuccess 180ms ease-in-out;
  transform: scale(1.3);
}

.success-icon__tip,
.success-icon__long {
  display: block;
  position: absolute;
  height: 6px; /* Increased line height */
  background-color: #6fd443; /* Specific color value */
  border-radius: 10px;
}

.success-icon__tip {
  width: 3em; /* Increased tip width */
  top: 50%; /* Adjusted top position to center vertically */
  left: 50%; /* Adjusted left position to center horizontally */
  transform: translate(-40%, -200%) rotate(45deg); /* Center the tick icon and rotate */
  animation: tipInPlace 300ms ease-in-out;
  animation-fill-mode: forwards;
  animation-delay: 180ms;
  visibility: hidden;
}

.success-icon__long {
  width: 5em; /* Increased long line width */
  transform: translate(-20%, -100%) rotate(-45deg); /* Center the tick icon and rotate */
  top: 50%; /* Adjusted top position to center vertically */
  left: 50%; /* Adjusted left position to center horizontally */
  animation: longInPlace 140ms ease-in-out;
  animation-fill-mode: forwards;
  visibility: hidden;
  animation-delay: 300ms; /* Adjust the delay as needed */
}

@keyframes showSuccess {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

@keyframes tipInPlace {
  from {
    width: 0em;
    top: 0em;
    left: -1.6em;
  }
  to {
    width: 3em;
    top: 5.2em;
    left: 1.8em;
    visibility: visible;
  }
}

@keyframes longInPlace {
  from {
    width: 0em;
    top: 6.4em; /* Adjusted top position */
    left: 3.8em; /* Adjusted left position */
  }
  to {
    width: 5em;
    top: 4.2em;
    left: 3.2em;
    visibility: visible;
  }
}
</style>
