<script>
export default {
    name: 'Chess'
}

</script>

<template>
    <div>
        <h2>棋类游戏</h2>
        <router-link to="/chess/tictactoe">井字棋</router-link>
    </div>
    <div>
        <router-view/>
    </div>
</template>

<style scoped>

</style>