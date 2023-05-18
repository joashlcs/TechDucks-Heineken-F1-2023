<template>
  <alert class="text-center" :message=message v-if="showMessage"></alert>
  <div class="form-group">
    <video id="qrScanner" class="qr-scanner-video"></video>
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
      scanner: null,
      message: '',
      showMessage: false,
      isValid: false,
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
    valid() {
      const payload = {
        "document_id": this.user_id,
        read: true
      };
      const path = `http://127.0.0.1:5000/${this.user_id}/cup-count`;

      axios.post(path, {
        headers: {
          'Content-Type': 'application/json'
        },
        params: payload
      })
        .then((response) => {
          return response;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    startScan() {
      const video = document.getElementById('qrScanner');
      QrScanner.hasCamera().then(hasCamera => {
        if (!hasCamera) {
          alert('Camera not found');
          return;
        }
        this.scanner = new QrScanner(video, result => {
          this.user_id = result.data;
          console.log(this.user_id)
          const response = this.valid()
          console.log(response)
          this.stopScan()
          if (response.data === '200') { //Check if user is present
            if (response.data >= 1) {
              this.stopScan()
              this.$router.push(`/returnuser/${this.user_id}`); // push to returning user page
            } else {
              this.stopScan()
              this.$router.push(`/reactiontest/${this.user_id}/firstbeer`); //push to new user page
            }
          } else {
            this.message = 'Invalid QR code or User. Please use a valid one';
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
