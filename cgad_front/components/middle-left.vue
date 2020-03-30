<template>
    <div>
        <img src = "~assets/ball.png" id="ball" />
       <img src = "~assets/bar.png" id = "bar"/>
     </div>   
</template>

<script>
export default {

    data: function(){
        return {
            altitude: 0,
            actualHeight: 0,
            topMargin: 0
        }
    },

    mounted(){
        bar = document.getElementById("bar")
        let y = bar.offsetTop
        let x = bar.offsetLeft
        let bar_width = bar.width
        let bar_height = bar.height
        console.log(x)
        console.log(y)
        
        let ball = document.getElementById("ball")

        let ball_height = ball.height
        let ball_width = ball.width

        ball.style.left = x - ball_width + bar_width*3/5  + "px" 
        ball.style.top = y - ball_width + "px"


        this.altitude = y - bar_height *4/3
        this.actualHeight = y - bar_height *4/3


        this.animateUp()


    },

    methods: {
        animateUp: function(){
            let ball = document.getElementById("ball")
            if (this.altitude > this.topMargin){
                ball.style.top = this.altitude + "px"
                this.altitude -= 5
                setTimeout(this.animateUp, 15)
            }
            else{
                this.animateDown()
            }
        },
        animateDown: function(){
            let ball = document.getElementById("ball")
            if (this.altitude < this.actualHeight){
                ball.style.top =this.altitude + "px"
                this.altitude += 5
                setTimeout(this.animateDown, 15)
            }
            else{
                let random_multiplier = Math.random()
                while (random_multiplier > 0.6){
                    random_multiplier = Math.random()
                }
                this.topMargin = this.actualHeight * random_multiplier

                console.log(this.topMargin)
                this.animateUp()
            }
        }
    }
}
</script>

<style scoped>

#bar{
    margin-top: 150%;
    margin-left: 20%;
    width: 120%;
}

#ball{
    height: 70px;
    width: 70px;
    position: absolute;
}

</style>

