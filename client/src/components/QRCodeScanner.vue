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
      if (this.user_id === '') {
        console.log("Missing document_id");
        return Promise.reject("Missing document_id");
      }

      const payload_landing = {
        document_id: this.user_id,
        read: true
      };
      const path = `https://techducks-api-app-drhnv.ondigitalocean.app/${this.user_id}/cup-count`;

      return axios.post(path, payload_landing, {
        headers: {
          'Content-Type': 'application/json'
        }
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
          console.log(`UserID is: ${this.user_id}`)
          this.valid()
            .then((response) => {
              console.log(response.data.cups)
              if (response.data.cups > 0) {
                this.stopScan()
                this.$router.push(`/returnuser/${this.user_id}`);
              } else {
                this.stopScan()
                this.$router.push(`/reactiontest/${this.user_id}/firstbeer`); //push to new user page
              }
            })
            .catch((error) => {
              this.message = 'Invalid QR code or User. Please use a valid one';
              this.showMessage = true;
              this.scanner.start();
            });
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
