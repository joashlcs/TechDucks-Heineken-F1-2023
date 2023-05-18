<template>
  <alert class="text-center" :message=message v-if="showMessage"></alert>
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
      cup_id: '',
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
    this.startScan();
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
          this.cup_id = result.data;

          if (this.user_id === this.cup_id) { // Check if cup belongs to user
            this.stopScan()
            this.$router.push(`/reactiontest/${this.user_id}/consecutivebeer`);
          } else {
            this.message = 'Please place your own cup into the holder below';
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
