<template>
  <div class="posts">
    <p>all posts</p>
    <p>{{ url }}</p>
    <p>{{ posts }}</p>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        url: process.env.API_URL + '/posts/',
        posts: [],
      }
    },
    methods: {
      async getPosts() {
        await this.$axios.get(process.env.API_URL + '/posts/')
          .then(res => {
            console.log(res.data);
            this.posts = res.data;
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    mounted() {
      this.getPosts();
    }
  }
</script>

<style scoped>

</style>
