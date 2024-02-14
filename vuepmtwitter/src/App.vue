<template>
  <div class="add_tweet" id="app">
      <form v-on:submit.prevent="createTweet">
          <div class="form-group">
              <label for="name">Name</label>
              <input type="text" class="form-control" id="name" v-model="tweet.name">
          </div>
          <div class="form-group">
              <label for="message">Message</label>
              <textarea class="form-control" id="message" v-model="tweet.message"></textarea>
          </div>
          
          <div class="form-group">
              <button type="submit">Add tweet</button>
          </div>
      </form>
  </div>
      <div class="tweets_container">
          <div class="tweets_content">
              <h1>Tweets</h1>
              <ul class="tweets_list">
                  <li v-for="tweet in tweets" :key="tweet.name">
                      <h5>{{tweet.name}}</h5>
                      <p>{{ tweet.message }}</p>
                      <p>{{ tweet.created_at }}</p>
                      
                      
                  </li>
              </ul>
          </div>
      </div>
  </template>
  
  
  
  <script>


      export default {
          name:'App',
          data() {
              return {
                tweet: {
                  name:'',
                  message:'',
                  created_at:''
                },
                  // tweet
                  tweets: [],
              }
          
          },
          async created(){
            await this.getTweets();
          },

  
          methods: {
              async getTweets(){
                  var response=await fetch ('http://127.0.0.1:8000/tweetsc/')
                  this.tweets = await response.json();
              },
            
              async createTweet(){
                await this.getTweets();

                await fetch('http://localhost:8000/tweetsc/', {
                  method: 'post',
                  headers:{
                    'Content-Type':'application/json'
                },
                  body: JSON.stringify(this.tweet)
                });
                // this.tweets.push(await response.json());
                await this.getTweets();

              },
              },
          };
          
      
  </script>