<template>
  <div>
    <input v-model="inputValue" @keyup.enter="submitData"/>
    <p>{{serverResponse}}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      inputValue: '',
    }
  },
  methods: {
    async submitData() {
      const response = await axios.post('http://localhost:5000/submit', { data: this.inputValue });
      this.serverResponse = response.data;
    }
  }
}
</script>