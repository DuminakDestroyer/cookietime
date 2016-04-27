import React from 'react';
import ReactDOM from 'react-dom';

var data = [];

var Comment = React.createClass({
  render: function() {
    return (
      <div className="comment">
        <h4 className="commentAuthor">
          {this.props.author}
        </h4>
                <p className = "message"> {this.props.children}</p>
                <p className = "log_time text-left">Logged at:  {this.props.time}</p>
      </div>
    );
  }
});


var CommentList = React.createClass({
  render: function() {
    var commentNodes = this.props.data.map(function(comment) {
      return (
        <Comment author={comment.author} key={comment.id} time={comment.time}>
          {comment.text}
        </Comment>
      );
    });
    return (
      <div className="commentList">
        {commentNodes}
      </div>
    );
  }
});

var CommentBox = React.createClass({
  loadCommentsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadCommentsFromServer();
    setInterval(this.loadCommentsFromServer, this.props.pollInterval);
  },
  render: function() {
    return (
      <div className="commentBox">
        <h3 className = "text-center">Message Board</h3>
        <CommentList data={this.state.data} />
      </div>
    );
  }
});

ReactDOM.render(
  <CommentBox url="api/messages" pollInterval={2000} />,
  document.getElementById('mainContainer')
);
