from django.shortcuts import render,redirect
from . models import Home,About,Hobbies,What_I_Do,Expertise_caption,Expertise_item,Comment,Footer,Footer_link,Copyright,Contact_Info
import random

# index function
def index(request):
  # ---comment-sec---
  if request.POST:
    first_name = request.POST.get('first-name')
    second_name = request.POST.get('second-name')
    comment = request.POST.get('comment')
    
    #random profile picture choose
    profiles = ['profile_3.jpg','profile_1.jpg','profile_2.jpg','comment.jpg']
    selected_profile = random.choice(profiles)

    # Comment model object
    comment_obj = Comment()
    comment_obj.first_name = first_name
    comment_obj.second_name = second_name
    comment_obj.comment = comment
    comment_obj.profile = selected_profile
    comment_obj.save()
    return redirect('index')

  #collecting data object from database
  home_data = Home.objects.all()
  about_data = About.objects.all()
  hobbies_data = Hobbies.objects.all()
  services_data = What_I_Do.objects.all()
  expertise_caption_data = Expertise_caption.objects.all()
  expertise_items_data = Expertise_item.objects.all()
  comment_data = Comment.objects.all()
  footer_data = Footer.objects.all()
  footer_link_data = Footer_link.objects.all()
  copyright_data = Copyright.objects.all()
  contact_info_data = Contact_Info.objects.all()


  #context dict sharing data to template
  context = {
    'homes':home_data,
    'abouts':about_data,
    'hobbies':hobbies_data,
    'services':services_data,
    'captions':expertise_caption_data,
    'expertises':expertise_items_data,
    'comments':comment_data,
    'footers':footer_data,
    'footer_links':footer_link_data,
    'copyrights':copyright_data,
    'contacts':contact_info_data,
  }
  return render(request,'index.html',context)
