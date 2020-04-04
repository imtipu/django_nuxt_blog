<template>
  <div>
    {{post_slug}}
    {{url}}
    {{post}}
  </div>
</template>

<script>
  export default {
    name: "_slug",
    data() {
      return {
        post_slug: this.$route.params.slug,
        url: process.env.API_URL + '/posts/' + this.$route.params.slug + '/',
        post: '',

      }
    },
    head(){
      return{
        title: this.post.title,
      }
    },
    methods: {
      async getPost() {
        await this.$axios.get(process.env.API_URL + '/posts/' + this.post_slug + '/')
          .then(res => {
            console.log(res.data);
            this.post = res.data;
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    mounted() {
      this.getPost();
    }
  }
</script>

<style scoped>

</style>
