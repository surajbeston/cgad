<template>
    <div id = "main-box" @click="adjustSize" >

        <div id = "search-box">
          <div id = "search-icon-box"> <img id = "search-icon" src = "~assets/Search.svg" /> </div><div id = "input-box-wrap" ><input id = "input-box" type = "text" @click = "deVaulter" v-model = "search_text" @blur="removeSuggestions" onclick="this.select()" autocomplete="off"/></div>
          
        </div>
        <div style="text-align: center;">
            <div id = "search-suggestion-box">
                <ul v-for="phone in phones" :key= "phone.name" class = "search-suggestion" @click="phoneRequester(phone)">
                    {{phone}}
                </ul>
            </div>
        </div>

        <div class = "product-detail-box">
            <h2 id = "phone-name">{{phone_name}}</h2>
            <div style= "" >
                <div  class = "product-image-box">
                        <img :src = "phone_image" class = "product-image" /> 
                </div>

                <div class = "specs-box">
                    <b-list-group>
                        <b-list-group-item><img src = "~assets/camera.svg" class = "feature-icon" /><div class = "specs">{{camera}}</div></b-list-group-item>
                        <b-list-group-item><img src = "~assets/ram.svg" class = "feature-icon" /><div class ="specs">{{specs.ram}}</div></b-list-group-item>
                        <b-list-group-item><img src = "~assets/battery.svg" class = "feature-icon" /><div class = "specs">{{specs.battery}}</div></b-list-group-item>
                        <b-list-group-item><img src = "~assets/Processor.svg" class = "feature-icon" /><div class = "specs">{{specs.processor}}</div></b-list-group-item>
                    </b-list-group>
                </div>   
            </div>
        </div>


        <div id = "search-result-box">
            <div  v-for ="product in products" :key = "product" class="search-result" >
                <div @click="phoneRedirect(product.url)">
                    <div class = "product-details" >
                        <div class = "name">{{product.name}} </div>
                        <div class = "price">Rs. {{product.price}}</div>
                        <div class = "platform">{{product.vendor}}</div>
                    </div>
        

                    <div class = "platform-banner">
                        <img :src = "product.brandLogoUrl" class = "banner-img">
                    </div> 
                </div>           
            </div>    
        </div> 


        <h2 class = "small-line" id ="small-line">/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////</h2>
    <div id = "phone-suggestion-wrap">
        <b-row >
            <b-col class = "phone-suggestion-box">
                <div class = "suggestion-image-box">
                    <img src = "https://images-na.ssl-images-amazon.com/images/I/51V8ObWrpKL._AC_SX569_.jpg" class = "suggestion-image">
                </div>
                <div class = "detail-box">
                    <h2 class = "price-suggestion"> Rs. 18, 232 </h2>
                    <h2 class = "name-suggestion">  Iphone X </h2>
                </div>
            </b-col>

            <b-col class = "phone-suggestion-box">
                <div class = "suggestion-image-box">
                    <img src = "https://images-na.ssl-images-amazon.com/images/I/51V8ObWrpKL._AC_SX569_.jpg" class = "suggestion-image">
                </div>
                <div class = "detail-box">
                    <h2 class = "price-suggestion"> Rs. 18, 232 </h2>
                    <h2 class = "name-suggestion">  Iphone X </h2>
                </div>
            </b-col>
        </b-row>

        <b-row>
            <b-col class = "phone-suggestion-box">
                <div class = "suggestion-image-box">
                    <img src = "https://images-na.ssl-images-amazon.com/images/I/51V8ObWrpKL._AC_SX569_.jpg" class = "suggestion-image">
                </div>
                <div class = "detail-box">
                    <h2 class = "price-suggestion"> Rs. 18, 232 </h2>
                    <h2 class = "name-suggestion">  Iphone X </h2>
                </div>
            </b-col>

            <b-col class = "phone-suggestion-box">
                <div class = "suggestion-image-box">
                    <img src = "https://images-na.ssl-images-amazon.com/images/I/51V8ObWrpKL._AC_SX569_.jpg" class = "suggestion-image">
                </div>
                <div class = "detail-box">
                    <h2 class = "price-suggestion"> Rs. 18, 232 </h2>
                    <h2 class = "name-suggestion">  Iphone X </h2>
                </div>
            </b-col>
        </b-row>
    </div>

    </div>        
</template>

<script>
export default {
    data: function (){
      return {
        phones: [
          ],
          phonesVault: [],
          products: [
              {price: "1,23,423", platform: "daraz.com", name: "Apple Iphone 64 GB 128 GB Exclusive"},
              {price: "34,58,745", platform: "okdam.com", name: "Apple Iphone 64 GB 128 GB Exclusive"}
          ],
          sessionId: {},
          search_text: "jkehfd",
          just_searched: false,
          phone_name: "Apple Iphone 11",
          slug: "",
          hasSessionId: false,
          phone_image: "https://images-na.ssl-images-amazon.com/images/I/51V8ObWrpKL._AC_SX569_.jpg",
          camera: "",
          specs: {"camera": "10 MP", "ram": "12 GB", "battery": "1200 MAh", "processor": "ARM Cortex 420"}
        }
    },

    methods: {
        deVaulter: function(){
            this.phones = this.phonesVault
            let all_names = document.getElementsByClassName("search-suggestion")
            if (all_names.length > 1 && !this.just_searched){
                document.getElementById("search-suggestion-box").style.display = "inline-block"
            }
            else{
                this.reVaulter()
            }
            this.just_searched = false
            console.log("De Vaulted!")
        },
        reVaulter: function(){
            document.getElementById("search-suggestion-box").style.display = "none";
        },
        phoneRequester: function(phone){
            console.log("Reached here");
            this.just_searched = true
            this.search_text = phone
            this.reVaulter()
            let slug = phone.replace(" ", "-")
            console.log(slug)
            this.$router.push(slug)            
        },
        removeSuggestions: function(){
            setTimeout(this.reVaulter, 200)
        },

        adjustSize: function(){
            let height = document.getElementById("search-result-box").offsetHeight
            let height1 = document.getElementById("search-suggestion-box").offsetHeight
            let height2 = document.getElementById("search-box").offsetHeight


            document.getElementById("small-line").style.marginTop = height + height1 + height2 + "px"

            let height3 = document.getElementById("small-line").offsetHeight
            let height4= document.getElementById("phone-suggestion-wrap").offsetHeight

            console.log(height4)

            document.getElementById("main-box").style.height = height + height1 + height2 + height3 + height4 *2   +"px"

            
            console.log("size adjusted")
            this.reVaulter()
        },

        adjustSpecs: function(){
            let listObjs = document.getElementsByClassName("specs")
            let maxLength = 0

            let textArr = []

            for (let index =0; index < 4; index++){
                let text = listObjs[index].innerHTML
                if (text.length > maxLength){
                    maxLength = text.length
                }
                textArr.push(text)
            }

            console.log(textArr)
            let newtextArr = []

            for (let index in textArr){
                let text = textArr[index]
                let space_length = maxLength - text.length
                let spaces = ""
                for (let i = 0; i < space_length; i++){
                    spaces += "&nbsp"
                }
                newtextArr.push(spaces + text)
            }

            for (let index in listObjs){
                if (index <= 3){
                listObjs[index].innerHTML = newtextArr[index]
                }
            }
        },
        async getSessionId() {
        let data = await this.$axios.$get('http://localhost:8000')
        this.sessionId = data["sessionId"]
        this.hasSessionId = true
        },
        async getSearchSuggestions(word){
            let that = this
            let data = await this.$axios.post('http://localhost:8000/search_suggest', {
                    sessionId: this.sessionId,
                    keyword: word
                })
                .then(function (response) {
                    that.phonesVault = response["data"]
                    that.deVaulter()
                    console.log(response["data"])
                })
                .catch(function (error) {
                    console.log(error);
                });
        },

        async getPhone(phone){
            let that = this
            console.log(this.sessionId)
            console.log(phone)
            console.log(phone)
            let data = await this.$axios.post('http://localhost:8000/find', {
                sessionId: this.sessionId,
                phone_name: phone
            })
            .then(function (response){
                console.log(response["data"])
                if (response["data"][1] != null){
                    console.log(response["data"][1])
                    that.products = response["data"][1]
                    that.phone_image = "http://localhost:8001/phone_images/" + response["data"][0]["image"]
                    that.phone_name = phone
                    that.search_text = phone
                    that.updateSpecs(response["data"][2])
                    that.$nextTick(() => {
                        that.adjustSize()
                     })
                }
            })
           .catch(function (error) {
               console.log("error section")
                console.log(error);
            });
        },
        doNothing: function(){
            console.log(this.hasSessionId)
            this.fetchData()
        },
        fetchData: function(){
            if (this.hasSessionId){
                let slug = this.$route.params.phone_name
                this.getPhone(slug.replace("-", " "))
            }
            else{
                setTimeout(this.doNothing, 100)
            }
        },
        phoneRedirect: function(url){
            window.open(url, '_blank');
        },
        updateSpecs: function(specs){
            let listObjs = document.getElementsByClassName("specs")
            listObjs[0].innerHTML = specs["camera"]
            listObjs[1].innerHTML = specs["ram"]
            listObjs[2].innerHTML = specs["battery"]
            listObjs[3].innerHTML = specs["processor"]
        }
    },
    watch: {
        search_text: function (val){
            console.log(this.just_searched)
            console.log(val.length)
            this.phonesVault = []
            if (val.length > 1 && !this.just_searched){
                console.log("sending request")
                this.getSearchSuggestions(val)
            }
        }
    },

    mounted() {
        this.adjustSize()
        window.addEventListener("resize", this.adjustSize)
        this.slug = this.$route.params.phone_name
       if (this.slug != ""){     
           console.log(this.sessionId)
           console.log(this.slug.replace("-", " "))      
        this.getPhone(this.slug.replace("-", " "))
        }

        
    },
    created(){
       this.getSessionId()
       this.fetchData()

    },
    destroyed() {
        window.removeEventListener("resize", this.adjustSize);
    },
}
</script>

<style scoped>


#main-box{
    overflow: hidden;
}

#search-icon-box{
    display: inline-block;
    border: 2px solid 5c6bc0;
    border-radius: 14px;
}

#search-icon-box:hover{
    background-color: rgba(255, 255, 255, 0.5);
    cursor: pointer;
}

#search-icon{
    height: 60px;
    width: 60px;
}

#input-box-wrap{
    display: inline-block;
    margin-left: 1%;
}

#input-box{
    height: 58px;
    border: 2px solid #5c6bc0;
    border-radius: 5px;
    font-size: 150%;
    font-family: 'Roboto Slab', serif;
    width: 600px;
    outline: none;
}

#search-box{
   text-align: center;
    margin-top: 5%;
}

#search-suggestion-box{
    border: 1px solid #5c6bc0;
    width: 600px;
    display: none;
    margin-left: 7%;
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
    }    

.search-suggestion{
    border-bottom: #5c6bc0 1px solid;
    padding-top: 5px;
    padding-bottom: 5px;
    margin: 0;
    font-family: 'Roboto Slab', serif;
}    

.search-suggestion:hover{
    background-color: #b2ebf2;
    cursor: pointer;
}

.feature-icon{
    height: 30px;
    margin-left: 10%;
    left: 0;
    position: absolute;
}

#search-result-box{ 
    position: absolute;
    left: 50%;
    margin-left: -270px;
    
}

.search-result{
    width: 600px;
    height: 120px;
    border-radius: 5px;
    background-color:#ffffff;
    /* background-image: linear-gradient(to right, #ffffff, #fffafa ); */
    margin-top: 5%;
    border: 2px solid #aaaa;
    box-shadow: 0px 0px 5px #aaaa;
    transition-duration: 0.5s;
    transition-timing-function: ease;
}


.search-result:hover{
    /* background-color: #abeafa; */
    cursor: pointer;
    box-shadow: 0px 0px 10px #aaaa;
    transform: scale(1.02);
}

.product-details{
    float: left;
    font-family: 'Roboto Slab', serif;
    margin-left: 10%;
}

.platform-banner{
    right: 5%;
    position: absolute;
    margin-top: 5%;
}

.banner-img{
    width: 150px;
    height: 50px;
    margin-top: 10%;
}

.price{
    font-size: 150%;
    margin-top: 3%;
    font-weight: 500;
    color: #0b1969;
}

.name{
    font-size: 150%;
    margin-top: 0;
    margin-left: -5%;
    font-weight: 400;
    color: #5c6bc0;
}

.platform{
    font-size: 70%;
    color: gray;
    text-decoration: underline;
}

.suggested-or-not{
    background-color: #5c6bc0;
    float: center;
    position: absolute;
    margin-top: 8%;
    margin-left: 40%;
    color: white;
    padding: 0 5px 0 5px;
    border-radius: 5px;
}

.suggestion-box{
        position: absolute;
    left: 50%;
    margin-left: -260px;
    background-color: #5c6bc0;
}

.small-line{
    color: #5c6bc0;
    font-family: 'Sen', sans-serif;
    text-decoration: underline overline;
    background-color: #4dd0e1;
}

.suggestion-image-box{
    text-align: center;
    height: 200px;
    transition-duration: 1s;
    transition-timing-function: ease;
}


.suggestion-image{
    height: inherit;
    display: inline-block;
    margin-top: 5%;
    margin-bottom: 5%;

}

.suggestion-image-box:hover{
    transform: scale(1.2)
}

.phone-suggestion-box{
    border: 1px solid #aaaa;
    margin: 5%;
    border-radius: 5px;
}

.phone-suggestion-box:hover{
    box-shadow: 0px 0px 5px #aaaa;
    cursor: pointer;
}

.detail-box{
    font-family: 'Roboto Slab', serif;
    margin-top: 15%;
    text-align: center;
    border-top: 1px solid #aaaa;
}

.price-suggestion .name-suggestion{
    color: #5c6bc0;
    font-size: 120%;
}

.name-suggestion{
    border: 2px #4dd0e1 solid;
    color: #0b1969;
    border-radius: 30px;
    padding: 1%;
    margin-left: 10%;
    margin-right: 10%;
}

.name-suggestion:hover{
    background-color: #abe8f0;

}

.product-detail-box{
    text-align: center;
}

.product-image-box{
    display: inline-block;
}

.product-image {
    height: 300px;
    margin-top: 5%;
    border-radius: 5px;
}

.specs-box{
    margin: 5% 20% 3% 25%;
    text-align: left;

}

.specs{
    color: #0b1969;
    font-weight: bold;
    margin-left: 20%;
    line-height: 2em;
    display: inline-block;

}

#phone-name{
    color: #0b1969;
    font-weight: bold;
    text-align: center;
    font-family: 'Roboto Slab', serif;
    border: 3px solid #0b1969;
    margin-left: 30%;
    margin-right: 30%;
    margin-top: 5%;
    border-radius: 10px;
}



@media only screen and (max-width: 1500px) {
    #search-icon{
        height: 55px;
        width: 55px;
    }

    #input-box{
        height:54px;
        font-size:145%;
        width: 550px;
    }

    #search-suggestion-box{
        width: 550px;
    }

    .small-line{
            font-size: 1.8em;
        }

}

@media only screen and (max-width: 1300px) {
    #search-icon{
        height: 50px;
        width: 50px;
    }

    #input-box{
        height:49px;
        font-size:140%;
        width: 500px
    }
    #search-suggestion-box{
        width: 500px;
    }    

    #search-result-box{ 
    position: absolute;
    left: 50%;

    margin-left: -220px;
    
    }

    .search-result{
        width: 500px;
        height: 110px;
    }

    .banner-img{
    width: 130px;
    height: 40px;
    }

    .name{
        font-size: 130%;
    }

    .price{
        font-size: 130%;
        margin-top: 5%;
    }

    .platform{
        font-size: 60%;
    }

    .suggested-or-not{
        font-size: 90%;
    }

    .small-line{
            font-size: 1.7em;
        }

}

@media only screen and (max-width: 1000px) {
    #search-icon{
        height: 40px;
        width: 40px;
    }

    #input-box{
        height:39px;
        font-size:120%;
        width: 400px
    }

    #search-suggestion-box{
        width: 400px;
        margin-left: 6%;
    }    

       #search-result-box{ 
    position: absolute;
    left: 50%;
    margin-left: -175px;
    
    }

    .search-result{
        width: 400px;
        height: 110px;
    }

    .banner-img{
    width: 100px;
    height: 30px;
    margin-top: 15%;
    }

    .name{
        font-size: 120%;
    }

    .price{
        font-size: 120%;
        margin-top: 0;
    }

    .platform{
        font-size: 60%;
    }

    .suggested-or-not{
        font-size: 70%;
    }

    .small-line{
            font-size: 1.6em;
        }


    
    .price-suggestion{
        font-size: 110%;
    }

    .name-suggestion{
        font-size: 110%;
    }

    .specs{
        font-size: 0.9em;
    }
    


}

@media only screen and (max-width: 700px) {
    #search-icon{
        height: 30px;
        width: 30px;
    }

    #input-box{
        height:30px;
        font-size:100%;
        width: 300px;
    }
    #search-suggestion-box{
        width: 300px;
        margin-left: 10%;
    }  

    #search-result-box{ 
        margin-left: -200px;
    
    }

    .search-result{
        width: 400px;
        height: 80px;
    }

    .banner-img{
    width: 70px;
    height: 23px;
    }

    .name{
        font-size: 100%;
    }

    .price{
        font-size: 100%;
        margin-top: 5%;
    }

    .platform{
        font-size: 50%;
    }

    .suggested-or-not{
        font-size: 50%;
        margin-left: 45%;
    } 

    .small-line{
            font-size: 1.5em;
    }


    .suggestion-image-box {
    height: 150px;
}



    .specs-box{
    margin: 5% 15% 3% 14%;
}


    #phone-name{
    font-size: 1.4em;

    }


    .price-suggestion{
        font-size: 90%;
    }

    .name-suggestion{
        font-size: 90%;
    }


    


}


@media only screen and (max-width: 600px) {
.price-suggestion{
    color: #5c6bc0;
    font-size: 120%;;
}

.name-suggestion{
    border: 2px #4dd0e1 solid;
    color: #0b1969;
    border-radius: 30px;
    padding: 1%;
    margin-left: 10%;
    margin-right: 10%;
    font-size: 120%;;
}

.specs-box{
 font-size:90%;   
margin: 5% 10% 3% 9%;
}


.phone-suggestion-box{
    border: 1px solid #aaaa;
    border-radius: 5px;
    margin: 2.5% 20% 2.5% 20%;
    }

.suggestion-image-box {
    height: 125px;
}


#search-result-box{ 
    position: absolute;
    left: 45%;


    margin-left: -165px;
    
    }

    .search-result{
        width: 400px;
        height: 90px; 

        margin-top: 10%;
    }


        .price-suggestion{
        font-size: 90%;
    }

    .name-suggestion{
        font-size: 90%;
    }


.suggestion-image-box:hover{
    transform: scale(1.1)
}


#phone-name{
    font-size: 1.3em;
    margin-left: 20%;
    margin-right: 20%;
}

.suggested-or-not{
    display: none;
} 

    #search-suggestion-box{

        margin-left: 7%;
    }
    .search-suggestion{
        text-align: left;
    }


}

@media only screen and (max-width: 450px) {


    #search-result-box{ 

        margin-left: -175px;
    }
    .search-result{
        height: 90px;
    }

    .specs-box{
        margin-left: 5%;
        margin-right: 5%;
        font-size: 0.8em;
    }


    .phone-suggestion-box{

        margin-left: 15%;
        margin-right: 15%;
    }


    #search-suggestion-box{

        margin-left: 10%;
    }

    .search-suggestion{
        text-align: left;
    }




}



@media only screen and (max-width: 400px) {
    #search-icon{
        height: 26px;
        width: 26px;
    }

    #input-box{
        height:25px;
        font-size:100%;
        width: 250px;
    }
    #search-suggestion-box{
        width: 250px;
    }    


    #search-result-box{ 
    margin-left: -130px;
    
    }

    .search-result{
        width: 300px;
        height: 90px;
    }

    .banner-img{
    width: 60px;
    height: 18px;
    margin-top: 20px;
    margin-right: 10px;
    }

    .name{
        font-size: 90%;
    }

    .price{
        font-size: 90%;
        margin-top: 0;
    }

    .platform{
        font-size: 45%;
    }

    .suggested-or-not{
        font-size: 45%;
        margin-left: 45%;
    }  


    .small-line{
            font-size: 1.15em;
        }

        .specs-box{
    margin: 5% 10% 3% 9%;
}    

    .specs-box{
        margin-left: 0;
        margin-right: 0;
    }

    .phone-suggestion-box{

        margin-left: 10%;
        margin-right: 10%;
    }




}




</style>