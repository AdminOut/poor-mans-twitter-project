<template>
  <div class="container add_tweet" id="app">
      <form v-on:submit.prevent="createTweet">
          <div class="row">
            <div class="column">
              <div class="form-group">
                  <label for="name" style="display: block;">Name</label>
                  <input type="text" class="form-control" id="name" style="height: 65px" v-model="tweet.name">
              </div>
            </div>
            <div class="column">
              <div class="form-group">
                  <label for="message" style="display: block;">Message</label>
                  <textarea class="form-control" id="message" v-model="tweet.message" maxlength="100"></textarea>
              </div>
            </div>
            <div class="column">
              <div class="form-group">
                <label style="display: block;">&#160;</label>
                  <button class="button button-outline" type="submit">Add tweet</button>
              </div>
            </div>
          </div>
      </form>
  </div>
  <div class="container tweets_container">
    <h1>Tweets</h1>
    <table>
        <thead>
            <tr>
                <th>
                  Name
                  <button class="button button-clear" @click="changeOrder('name')" style="font-size: large;">↑</button>
                  <button class="button button-clear" @click="changeOrder('-name')" style="font-size: large;">↓</button>
                </th>
                <th>Message</th>
                <th>
                  Created At
                  <button class="button button-clear" @click="changeOrder('created_at')" style="font-size: large;">↑</button>
                  <button class="button button-clear" @click="changeOrder('-created_at')" style="font-size: large;">↓</button>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="tweet in tweets" :key="tweet.id">
                <td>{{ tweet.name }}</td>
                <td>{{ tweet.message }}</td>
                <td>{{ tweet.created_at }}</td>
            </tr>
        </tbody>
    </table>
  </div>
</template>
  
  
  
  <script>


      export default {
          name:'App',
          data() {
              return {
                orderBy: '-created_at',
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
                const orderingQuery = `?ordering=${this.orderBy}`;
                var response = await fetch(`http://127.0.0.1:8000/tweets/${orderingQuery}`);
                this.tweets = await response.json();
              },
              changeOrder(orderBy) {
                this.orderBy = orderBy;
                this.getTweets();
              },
              async createTweet(){
                const response = await fetch('http://localhost:8000/tweets/', {
                  method: 'post',
                  headers:{
                    'Content-Type':'application/json'
                },
                  body: JSON.stringify(this.tweet)
                });
                this.tweets.push(await response.json());
                this.tweet = {
                  name:'',
                  message:'',
                  created_at:''
                }
              },
              },
          };
          
      
  </script>