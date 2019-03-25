import React, { Component } from 'react';
import './Colors.css';

class Colors extends Component {

	constructor(props) {
		super(props);
		this.state = {currColor: "black"};
		this.setState = this.setState.bind(this);
	}

	render() {
		return (
				<div>
					<CurrentColor currColor={this.state.currColor}/>
					<ColorButton name="red" setColor={this.setState}/>
					<ColorButton name="orange" setColor={this.setState}/>
					<ColorButton name="yellow" setColor={this.setState}/>
					<ColorButton name="green" setColor={this.setState}/>
					<ColorButton name="skyblue" setColor={this.setState}/>
					<ColorButton name="blue" setColor={this.setState}/>
					<ColorButton name="purple" setColor={this.setState}/>
					<ColorButton name="brown" setColor={this.setState}/>
					<ColorButton name="white" setColor={this.setState}/>
					<ColorButton name="black" setColor={this.setState}/>
				</div>
		)
	}
}

class ColorButton extends Component {

	constructor(props) {
		super(props);
		this.updateColor = this.updateColor.bind(this);
	}

	render() {
		return (
			<button className="ColorButton" id={this.props.name} onClick={this.updateColor}/>
		)
	}

	updateColor() {
		this.props.setColor({currColor: this.props.name});
	}
}

class CurrentColor extends ColorButton {

	render() {
		return (
			<button className="ColorButton" id="current" style={{backgroundColor: this.props.currColor}}/>
		)
	}
}

export default Colors;
