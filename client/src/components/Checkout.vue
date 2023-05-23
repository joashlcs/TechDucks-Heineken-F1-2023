<template>
  <div class="checkout-page">
    <div class="checkout-form">
      <div class="logo">
        <img class="fit-picture" src="../assets/heineken.png"/>
      </div>
      <h1 class="text-center underline text-black">Checkout</h1>
      <div class="card">
        <template v-if="this.type === 'beer'">
          <img class="img-limiter" src="../assets/heineken-draught-glass.png" alt="Product Image" />
          <div class="card-body">
            <h5 class="card-title text-center">Heineken Beer</h5>
            <p class="card-text-2 text-center">Discount: {{ this.beerDiscount }}%</p>
            <p class="card-text text-center">Price: ${{ this.beerPrice.toFixed(2) }}</p>
          </div>
        </template>
        <img v-else class="img-limiter-drinkaid" src="../assets/drinkaid.webp" alt="Product Image" />
        <div class="card-body">
          <h5 v-if="this.drinkaidDiscountType === 'free'" class="card-title text-center">DrinkAid<br>(1 serving: 2 pills)</h5>
          <h5 v-else v-if="this.type !== 'beer'" class="card-title text-center">DrinkAid<br>(6 serving: 12 pills)</h5>
          <p class="card-text-2 text-center" v-if="this.type !== 'beer'">Discount: {{ this.drinkaidDiscount }}%</p>
          <p class="card-text text-center" v-if="this.type !== 'beer'">Price: ${{ this.drinkaidPrice.toFixed(2) }}</p>
        </div>
      </div>
      <div v-if="this.type !== 'beer' && this.drinkaidDiscountType === 'free'" class="button-container">
        <div class="button-wrapper">
<!--          <button class="btn btn-primary-heineken btn-small" @click="cashlessMethod">Cash-less Payment</button>-->
          <h3 class="btn btn-primary-heineken text-center">Dispensing Now,<br>Please Collect Below!</h3>
        </div>
      </div>
      <div v-else class="button-container">
        <div class="button-wrapper">
          <button class="btn btn-primary-heineken btn-small" @click="cashlessMethod">Cash-less Payment</button>
          <span class="vertical-center"><b>OR</b></span>
          <button class="btn btn-primary-heineken btn-small" @click="cashMethod">Cash Payment</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'Checkout',
  data () {
    return {
      beerDiscount: 10,
      beerPrice: 10,
      drinkaidDiscount: 30,
      drinkaidPrice: 2.31,
      drinkaidDiscountType: null,
      userid: '',
      type: '',
      timeLeft: 6,
      landingPagePushed: false,
    }
  },
  created() {
    const resultData = this.$route.params;
    this.userid = resultData.id;
    this.type = resultData.product;
    this.drinkaidDiscountType = resultData.discount;
    this.getBeerDiscount()
    if (this.drinkaidDiscountType === 'free') {
      this.drinkaidDiscount = 100;
      this.drinkaidPrice = 0;
    } else {
      this.drinkaidDiscount = 30;
    }
    if (this.type !== 'beer' && this.drinkaidDiscountType === 'free') {
      this.startCountdown();
    }
  },
  methods: {
    startCountdown() {
      setInterval(() => {
        if (this.timeLeft > 0) {
          this.timeLeft--;
        } else {
          if (!this.landingPagePushed) {
            this.landingPagePushed = true;
            this.$router.push(`/leaderboard/${this.userid}`);
          }
        }
      }, 1000);
    },
    cashlessMethod () {
      let price;
      if (this.type === 'beer') {
        this.updateCupCount();
        price = this.beerPrice.toString().replace(".", "_")
      } else {
        price = this.drinkaidPrice.toString().replace(".", "_")
      }
      this.$router.push(`/payment/${this.userid}/cashless/${this.type}/${price}`);
    },
    cashMethod () {
      let price;
      if (this.type === 'beer') {
        this.updateCupCount();
        price = this.beerPrice.toString().replace(".", "_")
      } else {
        price = this.drinkaidPrice.toString().replace(".", "_")
      }
      this.$router.push(`/payment/${this.userid}/cash/${this.type}/${price}`);
    },
    updateCupCount() {
      if (this.userid === '') {
        console.log("Missing document_id");
        return Promise.reject("Missing document_id");
      }

      const payload_landing = {
        document_id: this.userid,
        read: true
      };
      const path = `https://5000-joashlaw75-techducks-htn4hymsh8o.ws-us97.gitpod.io/${this.userid}/cup-update`;

      return axios.post(path, payload_landing, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          console.log("Cup Count + 1")
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getBeerDiscount() {
      this.getBeerPercentageOff()
        .then((response) => {
          const data = response.data;
          this.beerDiscount = data.discount_percentage;
          this.beerPrice = data.final_price;
          console.log(this.beerDiscount)
          console.log(this.beerPrice)
        })
        .catch((error) => {
          console.log(error);
        })
    },
    getBeerPercentageOff() {
      if (this.userid === '') {
        console.log("Missing document_id");
        return Promise.reject("Missing document_id");
      }

      const payload_landing = {
        document_id: this.userid,
        read: true
      };
      const path = `https://5000-joashlaw75-techducks-htn4hymsh8o.ws-us97.gitpod.io/${this.userid}/discount`;

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
  }
}
</script>

<style scoped>
.checkout-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.checkout-form {
  margin-top: -40px !important;
  width: 300px;
  max-height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.underline {
  padding-bottom: 3px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  margin-bottom: 35px;
}

.card {
  width: 100%;
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.img-limiter {
  max-width: 200px;
  max-height: 300px;
  margin: -10px;
  transform: scale(0.85);
}

.img-limiter-drinkaid {
  max-width: 300px;
  max-height: 300px;
  margin: -10px;
  transform: scale(0.85);
}

.card-body {
  padding: 10px;
}

.card-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 5px;
}

.card-text {
  font-size: 17px;

}

.card-text-2 {
  font-size: 17px;
  margin-bottom: 0px;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 35px;
}

.btn-small {
  width: 110px;
}


.vertical-center {
  margin: 0px 15px;
}

.btn-primary-heineken {
  background-color: #007bff;
  color: white;
  font-weight: bold;
  padding-left: 10px !important;
  padding-right: 10px !important;
  display: block;
  transform: scale(1.1) !important;
  font-size: 1rem !important;
  border-radius: 15px !important;
  background-color: #038135 !important;
  color: white !important;
}

.button-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
}
</style>
