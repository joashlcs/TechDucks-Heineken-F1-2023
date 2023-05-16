<template>
  <div class="form-group">
    <video id="qrScanner" class="qr-scanner-video"></video>
  </div>
</template>

<script>
import QrScanner from 'qr-scanner';

export default {
  data() {
    return {
      qrResult: '',
      scanner: null
    };
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
          this.qrResult = result;
          this.stopScan();
          if (result.data === 'https://www.google.com') {
            // Require API request to see if user is first timer (API should return if QR code is new [TRUE] or old [False])
            this.$router.push('/reactiontest');
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
