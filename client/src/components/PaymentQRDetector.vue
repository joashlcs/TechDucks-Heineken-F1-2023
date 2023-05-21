<template>
  <alert class="text-center mb-2" :message=message v-if="showMessage"></alert>
  <div class="form-group">
    <video id="qrScanner2" class="qr-scanner-video"></video>
  </div>
</template>

<script>
import axios from "axios";
import QrScanner from 'qr-scanner';
import Alert from "@/components/Alert.vue";

export default {
  data() {
    return {
      user_id: '',
      payment_id: '',
      scanner: null,
      message: '',
      showMessage: false,
      isValid: false,
    };
  },
  components: {
    alert: Alert,
  },
  created() {
    const resultData = this.$route.params.id;
    this.user_id = resultData;
    console.log(`User ID: ${resultData}`);
  },
  mounted() {
    setTimeout(() => {
      this.startScan();
    }, 1000);
  },
  beforeDestroy() {
    this.stopScan();
  },
  methods: {
    startScan() {
      const video = document.getElementById('qrScanner2');
      QrScanner.hasCamera().then(hasCamera => {
        if (!hasCamera) {
          alert('Camera not found');
          return;
        }
        this.scanner = new QrScanner(video, result => {
          this.payment_id = result.data;

          if (this.payment_id === 'payment') {
            this.stopScan()
            this.$router.push(`/payment_success/${this.user_id}`);
          } else {
            this.message = 'Please use valid payment type!';
            this.showMessage = true;
            this.scanner.start();
            this.startScan();
          }
        }, { returnDetailedScanResult: true });
        this.scanner.start();
      });
    },
    stopScan() {
      if (this.scanner) {
        this.scanner.destroy();
        this.scanner = null;
      }
    }
  }
};
</script>

<style>
.qr-scanner-video {
  position: absolute;
  top: -9999px;
  left: -9999px;
  visibility: hidden;
}
</style>
