<script>
import SimpleButton from './components/SimpleButton.vue';

export default {
    data() {
        return {
            mssg: 'This is dynamic message'
        };
    },
    components: { SimpleButton }
}
</script>

<template>
  <div>
    <h1> Hello, welcome to Vue! </h1>
    <h2> {{ mssg }} </h2>
    <SimpleButton></SimpleButton>
  </div>
</template>

<style scoped>
</style>