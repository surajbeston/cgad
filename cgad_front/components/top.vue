<template>
  <div>
    <b-row>
      <b-col cols="5">
        <h1 class = "heading  head-right">Compare </h1>
      </b-col>
      <b-col cols="2" id = "img-head">
        <b-img class = "head-img" center src="~assets/logo.svg" alt="Left image"></b-img>
      </b-col>
      <b-col cols = "5">
        <h1 class = "heading  head-left">Gadjets</h1>
      </b-col>
    </b-row>

      <h1 class = "line">////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////</h1>


  </div>  
</template>

<style scoped>

  div{
    -webkit-user-select: none; /* Safari */
  -ms-user-select: none; /* IE 10+ and Edge */
  user-select: none; /* Standard syntax */
  }
  .head-img{
    height: 200px;
    margin-top: 3%;
  }

  .heading{
    color: white;
    font-family: 'Sen', sans-serif;
    text-align: center;
    margin-top: 7%;
    font-size: 500%;
    font-weight: bold;
    background-color: #5c6bc0;
  }


  .line{
    color: #5c6bc0;
    font-family: 'Sen', sans-serif;
    text-decoration: underline overline;
    background-color: #4dd0e1;
  }

  .head-right{
    text-align: right;
    border-top-right-radius: 50px;
    border-bottom-right-radius: 50px;
    padding-right: 2%;
    background-image: linear-gradient(to right, #a3acdb , #5c6bc0);
  }

  .head-left{
    text-align: left;
    border-top-left-radius: 50px;
    border-bottom-left-radius: 50px;
    padding-left: 2%;
    background-image: linear-gradient(to left, #a3acdb , #5c6bc0);
  }


  @media only screen and (max-width: 1500px) {
        .heading{
            font-size: 400%;
        }

        .head-img{
            height: 175px;
        }

        .line{
            font-size: 1.8em;
        }

  }

   @media only screen and (max-width: 1300px) {
        .heading{
            font-size: 375%;
        }

        .head-img{
            height: 150px;
        }

        .line{
            font-size: 1.7em;
        }
  }

     @media only screen and (max-width: 1300px) {
        .heading{
            font-size: 350%;
        }

        .head-img{
            height: 125px;
        }
        .line{
            font-size: 1.6em;
        }
  }

    @media only screen and (max-width: 1000px) {
        .heading{
            font-size: 300%;
        }

        .head-img{
            height: 100px;
        }
        .line{
            font-size: 1.5em;
        }
  }


      @media only screen and (max-width: 700px) {
        .heading{
            font-size: 275%;
        }

        .head-img{
            height: 90px;
        }
        .line{
            font-size: 1.4em;
        }
  }


      @media only screen and (max-width: 650px) {
        .heading{
            font-size: 250%;
        }

        .head-img{
            height: 80px;
        }
        .line{
            font-size: 1.3em;
        }



  }

        @media only screen and (max-width: 550px) {
        .heading{
            font-size: 200%;
        }

        .head-img{
            height: 70px;
        }
        .line{
            font-size: 1.2em;
        }
  }

          @media only screen and (max-width: 450px) {
        .heading{
            font-size: 175%;
        }

        .head-img{
            height: 50px;
        }
        .line{
            font-size: 1.15em;
        }
  }


            @media only screen and (max-width: 400px) {
            .head-img{
            height: 43px;
        }
            }


            @media only screen and (max-width: 350px) {
        .heading{
            font-size: 145%;
        }

        .head-img{
            height: 39px;
        }
        .line{
            font-size: 1em;
        }
            .head-right{
              padding-right: 15%;
          }

  }

</style>