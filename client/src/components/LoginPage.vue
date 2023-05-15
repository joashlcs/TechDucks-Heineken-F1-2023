<template>
  <div className="d-flex flex-wrap justify-content-center align-items-center flex-column" style="height: 100vh;">
    <div className="logo">
      <img className="fit-picture" src="../assets/heineken.png"/>
    </div>
    <div className="container col-md-6">
      <div className="card">
        <div className="card-header">Scan QR Code</div>
        <div className="card-body">
          <div className="form-group">
            <label htmlFor="result">Result</label>
            <textarea className="form-control" id="result" rows="3" v-model="qrResult"></textarea>
          </div>
          <div className="form-group">
            <video id="qrScanner" width="100%" style="object-fit: cover;"></video>
          </div>
        </div>
      </div>
    </div>
    <audio ref="beepSound" src="../assets/beep.mp3"></audio>
  </div>
</template>

<script>
import QrScanner from 'qr-scanner';

export default {
  data() {
    return {
      qrResult: '',
      scanner: null
    }
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
          this.$refs.beepSound.currentTime = 0;
          this.$refs.beepSound.play();
          this.stopScan();
          if (result === 'https://www.google.com') {
            // Require API request to see if user is first timer (API shld return if QR code is new [TRUE] or old [False])
            this.$router.push('/reactiontest');
          }
        });
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
textarea {
  resize: none;
}
</style>
