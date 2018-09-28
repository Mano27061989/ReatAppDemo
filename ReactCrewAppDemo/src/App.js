import React from "react";
import Weather from "./components/weather";
import Form from "./components/form";
import ReactTable from "react-table";
import 'react-table/react-table.css';
import rcprogress from 'rc-progress';


// import SWeather from "./components/stateless_weather";
// import SForm from "./components/stateless_form"
import Titles from "./components/titles";
var Line = rcprogress.Line;
var Circle = rcprogress.Circle;


const Api_Key = "8d2de98e089f1c28e1a22fc19a24ef04";
let i=0;
class App extends React.Component {

  state = {

    temperature: undefined,
    city: undefined,
    country: undefined,
    humidity: undefined,
    description: undefined,
    error: undefined,
    data: undefined,

  }

  getData =  async function(){
    i=i+1;
    //const api_call = await fetch('http://192.168.56.104:8081/listUsers');
  const api_call = await fetch('http://192.168.56.104:8080/API/User/getUserStats');
      const response = await api_call.json();
  //    console.log(response)
      this.setState({

     data:response.userInfoRespList


    })
    this.state.cpu=response.cpu
    this.state.mem=response.mem
    this.state.disk=response.disk
    console.log(response.cpu)
  }

  loopFn = function(){
    setInterval(() =>{ this.getData()}, 1000);
    console.log('loop fn');
  }

  componentDidMount =   function(){
      this.loopFn();

  }



  render() {

    const columns = [{
    Header: 'UserSrcIP',
    accessor: 'userIp' // String-based value accessors!
  }, {
    Header: 'DestIP',
    accessor: 'destIp',
  //  Cell: props => <span className='number'>{props.value}</span> // Custom cell components!
  }, {
  //  id: 'friendName', // Required because our accessor is not a string
    Header: 'TimeStamp',
    accessor: 'timeStamp' // Custom value accessors!
  }, {
    Header: props => <span>HTTP Code</span>, // Custom header components!
    accessor: 'status'
  }]

    return (

      <div>
         <div className="wrapper">
          <div className="main">
          <div className="container">

          <div>
                          <div className="circleCtr">
                            <Circle percent={this.state.cpu} strokeWidth="4" strokeColor="#1e9bf6" className="circle"/>
                            <h3 className="circleLabel"> CPU - {this.state.cpu}%</h3>
                          </div>
                        </div>

                        <div>
                                        <div className="circleCtr">
                                          <Circle percent={this.state.mem} strokeWidth="4" strokeColor="#d680d6" className="circle"/>
                                          <h3 className="circleLabel"> MEM - {this.state.mem}%</h3>
                                        </div>
                                      </div>
                                      <div>
                <div className="circleCtr">
                  <Circle percent={this.state.disk} strokeWidth="4" strokeColor="#d68080" className="circle"/>
                  <h3 className="circleLabel"> DISK - {this.state.disk}%</h3>
                </div>
              </div>


          </div>
            <div className="container">
              <ReactTable
                data={this.state.data}
                columns={columns}
              />
              <div className="row">
                <div>

                </div>
              </div>
            </div>
          </div>
        </div>


      </div>

    )
  }
}
export default App;
