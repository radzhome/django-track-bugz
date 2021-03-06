from django.db import models

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings


ACTIVE = 'A'
STATUS_CODES = (
    (ACTIVE, _('Active')),
    ('P', _('In progress')),
    ('R', _('Resolved')),
    ('C', _('Closed')),
)

PRIORITY_CODES = (
    (1, _('High')),
    (2, _('Medium')),
    (3, _('Low')),
)

# Make into own so can modify TODO
BUG = 'B'
TICKET_TYPES = (
    (BUG, _('Bug')),
    ('T', _('Task')),
    ('F', _('Feature')),
    ('E', _('Enhancement')),
    ('I', _('Inquiry')),
)

# LOG_TYPES = (
#     (1, _('Update')),
#     (2, _('Comments')),
# )

# judge ideas:
# https://github.com/orges/ITSY/blob/master/project/models.py
# https://github.com/trojkat/doner/blob/master/doner/project/models.py


class Project(models.Model):

    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(verbose_name=_('Description'), max_length=250, blank=True)
    #is_private = models.BooleanField(verbose_name=_('Private'), default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    #members = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='projects')
    #members_number = models.IntegerField(default=0, editable=False)
    #have_milestones = models.BooleanField(default=False, editable=False)


    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ('id',)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    # def get_absolute_url(self):
    #     return reverse('project', kwargs={'pk': self.pk})


class Milestone(models.Model):

    project = models.ForeignKey(Project, verbose_name=_('Project'))
    version_tag = models.CharField(verbose_name=_('Name'), max_length=50)
    #description = models.TextField(verbose_name=_('Description'), blank=True)
    start_date = models.DateField(verbose_name=_('Start Date'), blank=True, null=True)
    end_date_scheduled = models.DateField(verbose_name=_('Scheduled End Date'), blank=True, null=True)
    end_date_actual = models.DateField(verbose_name=_('Actual End Date'), blank=True, null=True)

    class Meta:
        verbose_name = _('Milestone')
        verbose_name_plural = _('Milestones')
        ordering = ('-id', )

    def __unicode__(self):
        #return u'%s - %s' % (self.project,  self.version_tag)
        return self.version_tag


class TicketItem(models.Model):  # this should be changed, TicketItem ?

    text = models.TextField(verbose_name=_('Text'), blank=True)  # Note
    attachment = models.FileField(upload_to='attachments/', help_text='(optional)')
    created_date = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    ticket = models.ForeignKey('track_bugz.Ticket', blank=False, null=False)
    #user (char field), link out to thumbnail image
    user = models.CharField(verbose_name=_('User'), max_length=255)  # update on save

    class Meta:
        verbose_name = _('Comment/Attachment')
        verbose_name_plural = _('Comments/Attachments')
        ordering = ('-id', )

    def __str__(self):
        return self.attachment.name.replace('attachments/', '')


class Ticket(models.Model):

    project = models.ForeignKey(Project, verbose_name=_('Project'))
    milestone = models.ForeignKey(Milestone, verbose_name=_('Milestone'), null=True, blank=True)
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    creation_date = models.DateTimeField(verbose_name=_('Submited date'), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_('Modified date'), auto_now=True)

    #TODO: Should be CharField ? Or have 2 fields?
    opened_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Opened By'), related_name='opened_by')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Assigned to'), null=True, blank=True)

    status = models.CharField(verbose_name=_('Status'), default=ACTIVE, choices=STATUS_CODES, max_length=1)
    priority = models.IntegerField(verbose_name=_('Priority'), default=3, choices=PRIORITY_CODES)
    ticket_type = models.CharField(verbose_name=_('Ticket type'), default=BUG, choices=TICKET_TYPES, max_length=1)
    #hours_spent =  ? / complexity
    #dependency = ?  # To achieve sub_ticket status
    #attachments = models.ManyToManyField(Attachment, null=True, blank=True)

    # Devise a way to have 1 level of subtickets only.

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ('priority', 'title')

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('ticket', kwargs={'pk': self.pk})

    def get_related_users_ids(self):
        '''
        Get ids of users related to this ticket.
        :rtype: set of integers
        :return: user ids
        '''
        # get user ids from log
        users_ids = set(self.log_set.all().order_by('author').values_list('author', flat=True).distinct())

        # add id of ticket submitter
        users_ids.add(self.submitter.id)

        if self.assigned_to:
            # add id of assigned user
            users_ids.add(self.assigned_to.id)

        return users_ids


