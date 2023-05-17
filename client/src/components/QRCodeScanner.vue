<template>
  <alert class="text-center" :message=message v-if="showMessage"></alert>
  <div class="form-group">
    <video id="qrScanner" class="qr-scanner-video"></video>
  </div>
</template>

<script>
import QrScanner from 'qr-scanner';
import Alert from "@/components/Alert.vue";

export default {
  data() {
    return {
      qrResult: '',
      scanner: null,
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  mounted() {
    this.startScan();
  },
  beforeDestroy() {
    this.stopScan();
  },
  methods: {
    startScan() {
      const video = document.getElementById('qrScanner');
      QrScanner.hasCamera().then(hasCamera => {
        if (!hasCamera) {
          alert('Camera not found');
          return;
        }
        this.scanner = new QrScanner(video, result => {
          this.qrResult = result.data;
          if (result.data === '12345678') {
            // Require API request to see if user is first timer (API should return if QR code is new [TRUE] or old [False])
            this.stopScan()
            this.$router.push(`/reactiontest/${result.data}`);
          } else {
            this.message = 'Invalid QR code. Please use a valid one';
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
