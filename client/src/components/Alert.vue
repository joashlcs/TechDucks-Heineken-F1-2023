<template>
  <div>
    <div class="alert alert-danger mb-0" role="alert">{{ message }}</div>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
