<template>
  <div>
    <div id="video-container"></div>
    <div id="result-container">{{ result }}</div>
  </div>
</template>

<script>
import Quagga from 'quagga';

export default {
  name: 'QrScanner1',
  data() {
    return {
      result: ''
    }
  },
  mounted() {
    Quagga.init({
      inputStream: {
        name: "Live",
        type: "LiveStream",
        constraints: {
          width: { min: 640 },
          height: { min: 480 },
          aspectRatio: { min: 1, max: 100 },
          facingMode: "environment" // or "user" for the front camera
        },
        target: document.querySelector('#video-container')
      },
      decoder: {
        readers: ['ean_reader', 'code_128_reader', 'code_39_reader', 'code_39_vin_reader', 'codabar_reader', 'upc_reader', 'upc_e_reader', 'i2of5_reader', '2of5_reader', 'code_93_reader'],
        debug: {
          drawBoundingBox: true,
          showFrequency: false,
          drawScanline: true,
          showPattern: false
        }
      }
    }, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      Quagga.start();
    });

    Quagga.onDetected(this.onDetected);
  },
  beforeDestroy() {
    Quagga.offDetected(this.onDetected);
    Quagga.stop();
  },
  methods: {
    onDetected(result) {
      this.result = result.codeResult.code;
    }
  }
}
</script>

<style>
#video-container {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
}

#result-container {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  color: #fff;
  padding: 10px;
}
</style>
