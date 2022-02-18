// HOME PAGE JS

var lstContainer = document.getElementById("myLIST");


var btnList = lstContainer.getElementsByClassName("li");


for (var i = 0; i < btnList.length; i++) {
  btnList[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
function deletefile(file_id) {
  Swal.fire({
    title: 'Are you sure?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, Put this file in Archive'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Archived',
        'Your file has been sent to Archive.',
        'success'
      ).then((result) => {
        window.location.href = "../delete_file/" + "?file_id=" + file_id
      })
    }
  })
}
function loginalert() {
  Swal.fire({
    icon: 'error',
    title: 'Oops...',
    text: 'Ivalid Username or password'
  })
}

function deleteaccountalert() {
  Swal.fire({
    title: 'Are you sure?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, Delete my Account'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Deleted',
        'Your Account has been Deleted',
        'success'
      )
    }
  })
}
function deleteuser(user_id) {
  Swal.fire({
    title: 'Are you sure you want to archive this User?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Delete this User'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Archived',
        'Done. Check this user in archive list.',
        'success'
      ).then((result) => {
        window.location.href = "../delete_user/" + "?user_id=" + user_id
      })
    }
  })
}
function restoreuser(user_id) {
  Swal.fire({
    title: 'Are you sure you want to retrieve this User?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Retrieve this User'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Restored',
        'Done. Successfully Restored this User.',
        'success'
      ).then((result) => {
        window.location.href = "../retrieve_user/" + "?user_id=" + user_id
      })
    }
  })
}
function deletefilepermanently(file_id) {
  Swal.fire({
    title: 'Do you want to Delete this file permenantly?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Delete File Permanently'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Deleted',
        'This File has been Deleted Permanently',
        'success'
      ).then((result) => {
        window.location.href = "../permanent_delete_file/" + "?file_id=" + file_id
      })
    }
  })
}

function restorefile(file_id) {
  Swal.fire({
    title: 'Do you want to Restore this file?',
    showDenyButton: true,
    confirmButtonText: 'Restore',
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
      Swal.fire('Restored!', '', 'success').then((result) => {
        window.location.href = "../retrieve_file/" + "?file_id=" + file_id
      })
    } else if (result.isDenied) {
      Swal.fire('File not Restored', '', 'info')
    }
  })
}


function deleteuserpermanently(user_id) {
  Swal.fire({
    title: 'Do you want to Delete this User permanently?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Delete User Permanently'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Deleted',
        'This User has been Deleted Permanently',
        'success'
      ).then((result) => {
        window.location.href = "../permanent_delete_user/" + "?user_id=" + user_id
      })

    }
  })
}

function userClick() {
  document.getElementById('user-type').value = "User";
  console.log(document.getElementById('user-type').value);
}
function adminClick() {
  document.getElementById('user-type').value = "Admin";
  console.log(document.getElementById('user-type').value);
}

$('#user_search_input').on('keyup', function (e) {
  e.preventDefault();

  $.ajax({
    type: 'get',
    url: "/User/",
    data: {
      search: $('#user_search_input').val()
    },
    success: function (data) {
      $('#table').html(data.rendered_table);
    },
    error: function (data) {
      alert('have an error');
    },
  });
});

$('#user_file_archive').on('keyup', function (e) {
  e.preventDefault();

  $.ajax({
    type: 'get',
    url: "/UserArchive/",
    data: {
      search: $('#user_file_archive').val()
    },
    success: function (data) {
      $('#table').html(data.rendered_table);
    },
    error: function (data) {
      alert('have an error');
    },
  });
});

$('#admin_search_input').on('keyup', function (e) {
  e.preventDefault();

  $.ajax({
    type: 'get',
    url: "/Admin/",
    data: {
      search: $('#admin_search_input').val()
    },
    success: function (data) {
      $('#table').html(data.rendered_table);
    },
    error: function (data) {
      alert('an error');
    },
  });
});

$('#admin_user_search').on('keyup', function (e) {
  e.preventDefault();

  $.ajax({
    type: 'get',
    url: "/AdminUserTab/",
    data: {
      search: $('#admin_user_search').val()
    },
    success: function (data) {
      $('#table').html(data.rendered_table);
    },
    error: function (data) {
      alert('an error');
    },
  });
});
$('#admin_user_archive').on('keyup', function (e) {
  e.preventDefault();

  $.ajax({
    type: 'get',
    url: "/AdminArchive/",
    data: {
      search: $('#admin_user_archive').val()
    },
    success: function (data) {
      $('#table').html(data.rendered_table);
    },
    error: function (data) {
      alert('an error');
    },
  });
});

$('#admin_file_archive').on('keyup', function (e) {
  e.preventDefault();

  $.ajax({
    type: 'get',
    url: "/AdminFileArchive/",
    data: {
      search: $('#admin_file_archive').val()
    },
    success: function (data) {
      $('#table').html(data.rendered_table);
    },
    error: function (data) {
      alert('an error');
    },
  });
});

$('#activity_report_logs').on('keyup', function (e) {
  e.preventDefault();

  $.ajax({
    type: 'get',
    url: "/AdminReport/",
    data: {
      search: $('#activity_report_logs').val()
    },
    success: function (data) {
      $('#table').html(data.rendered_table);
    },
    error: function (data) {
      alert('an error');
    },
  });
});

formlogout.addEventListener("click", function (event) {
  event.preventDefault();
  Swal.fire({
    title: 'Logout',
    text: "Are you sure you want to logout?",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes'
  }).then((result) => {
    if (result.isConfirmed) {
      document.getElementById("logoutform").submit();
    }
  })
})

function transferUserToArchive() {
  Swal.fire({
    title: 'Account Deletion',
    text: "Are you sure you delete your account?",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes'
  }).then((result) => {
    if (result.isConfirmed) {
      document.getElementById("deleteuser").submit();
    }
  })
}

$(window).on('load', function () {
  $('#id_file_name__icontains').attr('placeholder', 'File Name')
  $('#id_uploader__icontains').attr('placeholder', 'Uploader')
  $('#id_start_date').get(0).setAttribute('type', 'date');

  $('#id_file_type__icontains')
    .replaceWith(
      '<select id="id_file_type__icontains" name="file_type__icontains">' +
      '<option value="" disabled selected>Select file category</option>' +
      '<option value="audio">Audio</option>' +
      '<option value="video">Video</option>' +
      '<option value="image">Image</option>' +
      '<option value="text">Text</option>' +
      '</select>'
    );

})

function clearform() {
  document.getElementById("form_filter").reset();
}



$(document).ready(function () {
  $('#m_table').dataTable({ searching: false, paging: false, info: false });
  $('#m_table').DataTable();
});