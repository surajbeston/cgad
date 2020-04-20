<template>
    <div id = "main-box">
        <b-row>
            <b-col xl = "6">
                <div id = "question-box">
                    <img src = "~assets/robot.svg" id = "server-illus">
                    <h2 id = "description">We employ a robot that periodically checks e-commerce sites with proper consent and fetches results, which enables us to sort and present 
                        comparisons on demand.</h2>
                    
                </div>    
            </b-col>   
            <b-col xl = "6"> 
                <h2 id = "association">With Support of: </h2>
                    <b-row id = "link-box">
                        
                        <b-col id = "link-box-left">
                            <a href = "#" class = "association-link">daraz</a>
                            <a href = "#" class = "association-link">dealayo</a>
                            <a href = "#" class = "association-link">evostore</a>
                            
                        </b-col>   

                        <b-col>
                            <a href = "#" class = "association-link">muncha</a>
                            <a href = "#" class = "association-link">neostore</a>
                            <a href = "#" class = "association-link">okdam</a>
                        </b-col>    

                        <b-col id = "link-box-left">

                            <a href = "#" class = "association-link">olizstore</a>
                            <a href = "#" class = "association-link">pasalnepal</a>
                            <a href = "#" class = "association-link">reddoko</a>

                        </b-col> 

                        <b-col>
                            <a href = "#" class = "association-link">sastodeal</a>
                            <a href = "#" class = "association-link">smartdoko</a>
                            <a href = "#" class = "association-link">thulo</a>

                        </b-col>    
                    </b-row>  

                    <hr />

                    <b-row id = "shoutout-box">
                        <b-col>
                            <a href = "#" class = "shoutout-link">shoutout to development</a>
                        </b-col>
                        <b-col>
                            <a href = "#" class = "shoutout-link">shoutout to management</a>
                        </b-col>

                    </b-row>   


                    <hr /> 


                    <b-row id = "icons-group">

                        <b-col>
                            <img src = "~assets/facebook1.svg" class = "sm-icon">
                        </b-col> 

                        <b-col>
                            <img src = "~assets/instagram1.svg" class = "sm-icon">
                        </b-col>

                        <b-col>
                            <img src = "~assets/pinterest1.svg" class = "sm-icon">
                        </b-col>  
                     </b-row>   

                     <p id = "copyright"> Compare Gadjets, Dharan <br>&copy 2020 CGAD </p>

            
            </b-col>
        </b-row>  
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>

#main-box{
    background-color: #5c6bc0;
}

#description{
    color: white;
    font-family: 'Dosis', sans-serif;
    text-align: center;
}

#question-box{
    margin: 10%;
}

#server-illus{
    height: 500px;
    margin-left: 15%;
    margin-top: -10%;
}

#association{
    font-family: 'Dosis', sans-serif;
    color: white;
    font-size: 200%;
    margin-top: 5%;
    margin-left: 25%;
    margin-right: 25%;
    text-align: center;
    border-radius: 10px;
    font-weight: bolder;
}

#link-box{
    margin-top: 5%;
}

.association-link{
    color: #ffe5e5;
    font-family: 'Dosis', sans-serif;
    display: block;
    font-size: 125%;
    text-align: center;
}

#link-box-left{

}

hr{
    margin: 5%;
}

#shoutout-box{
    margin-left: 15%;

}

.shoutout-link{
    background-color: #ffe5e5;
    font-family: 'Dosis', sans-serif;
    font-size: 125%;
    text-align: center;
    padding: 2px 15px 3px 15px;
    border-radius: 15px;
}

.shoutout-link:hover{
    background-color: #ffb3b3;
}

#icons-group{
    margin-left: 30%;
    margin-right: 30%;
}

.sm-icon{
    height: 75px;
}

.sm-icon:hover{
    cursor: pointer;
}

#copyright{
    margin-top: 5%;
    text-align: center;
    color: white;
}


@media only screen and (max-width: 1600px) {

#icons-group{
    margin-left: 20%;
    margin-right: 20%;
}
}

@media only screen and (max-width: 1500px) {

#description, #association{

    font-size: 180%;
}

#link-box{
   margin-top: 5%;
}

.association-link, .shoutout-link, #copyright{
    font-size: 100%;
}

#server-illus{
    height: 400px;
    margin-left: 15%;
    margin-top: -10%;
}

}

@media only screen and (max-width: 1200px) {
    #description{

    font-size: 160%;
    margin-left: 20%;
    margin-right: 20%;
}

#association{
    font-size: 160%;
}

#link-box{
   margin-top: 5%;
}

.association-link, .shoutout-link, #copyright{
    font-size: 90%;
}

#server-illus{
    height: 400px;
    margin-left: 30%;
    margin-top: -10%;
}

}

@media only screen and (max-width: 900px) {
    #description{

    font-size: 150%;
    margin-left: 15%;
    margin-right: 15%;
}

#association{
    font-size: 150%;
}

#link-box{
    margin-top: 5%;
}

.association-link, .shoutout-link, #copyright{
    font-size: 85%;
}

#server-illus{
    height: 350px;
    margin-left: 25%;
    margin-top: -10%;
}

#icons-group{
    margin-left: 30%;
    margin-right: 30%;
}

.sm-icon{
    height: 60px;
}

}


@media only screen and (max-width: 700px) {
    #description{

    font-size: 130%;
    margin-left: 10%;
    margin-right: 10%;
}


#association{
    font-size: 130%;
}

#link-box{
    margin-top: 5%;
}

.association-link, .shoutout-link, #copyright{
    font-size: 80%;
}

#server-illus{
    height: 300px;
    margin-left: 15%;
    margin-top: -10%;
}

.sm-icon{
    height: 50px;
}

#icons-group{
    margin-left: 25%;
    margin-right: 25%;
}

#shoutout-box{
    margin-left: 10%;
}




}


@media only screen and (max-width: 500px) {
#icons-group{
    margin-left: 20%;
    margin-right: 20%;
}

}

@media only screen and (max-width: 400px) {
    #description{

    font-size: 110%;
    margin-left: 10%;
    margin-right: 10%;
}

#association{
    font-size: 110%;
}

#link-box{
    margin-top: 5%;
}

.association-link, .shoutout-link, #copyright{
    font-size: 80%;
}

#server-illus{
    height: 250px;
    margin-left: 10%;
    margin-top: -10%;
}

.sm-icon{
    height: 40px;
}

#icons-group{
    margin-left: 20%;
    margin-right: 20%;
}

#shoutout-box{
    margin-left: 0%;
}

}




</style>