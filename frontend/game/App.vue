<template>
    <div class="app">
        <h2>你好</h2>
        <router-link :to="{name:'GomokuGame'}">GomokuGame</router-link>
    </div>
    <div>
        <router-view></router-view>
    </div>
</template>

<script>

export default {
    name: 'Game',
};

</script>

<style>
</style>
