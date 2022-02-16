import videoImg from '../../assets/img/dua-lipa.jpg'
import React from 'react';

const PrincipalSection = () => {
    return (
        <>
            <div className="container-fluid App-main">
                <div className="container App-background">
                    <div className="row align-items-center">
                        <div className="col-md-12"> 
                            <h1>
                                <p>FUTURE</p> 
                                <p>NOSTALGIA</p>
                            </h1>
                        </div>
                        <div className="col-md-12">
                            <span>Lorem ipsum dolor at siamet</span>
                        </div>
                        <div className="col-md-12">
                            <button className="btn btn-primary">Buy Tickets</button>
                        </div>
                    </div>
                </div>
            </div>
            <div className="container">
                <div className="row">
                    <div className="col-md-6 mt-5">
                        <i className="fas fa-angle-down"></i>
                        <p>Did you see the last video</p>
                        <h2>LAST LP</h2>
                    </div>
                    <div className="col-md-6 mt-5 mb-4">
                        <img src={ videoImg } alt="" />
                    </div>
                </div>
            </div>
            <hr />
            <div className="container">
                <h1>Tickets goes here</h1>
            </div>
        </>
    )
}

export default PrincipalSection;