<script>
import { ref } from 'vue';

export default {
    setup() {
        const count = ref(0)
        return { count }
    }
}
</script>

<template>
    <button @click="count++">Clicked {{ count }} times</button>
</template>

<style scoped>

</style>