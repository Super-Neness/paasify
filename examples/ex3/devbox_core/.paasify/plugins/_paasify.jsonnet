local paasify = import 'paasify.libsonnet';

local plugin = {

  // Provides plugin metadata
  metadata: {
      name: "Paasify std lib",
      description: '',

      author: "mrjk",
      email: '',
      license: '',
      version: '',

      require: '',
      api: 1,
      schema: {},
    },

  // Return global vars
  default_vars(vars)::
    local dir_prefix = vars.stack_path + '/';
    {

      # Default settings
      # --------------------------

      app_name: vars.stack_name,
      app_domain: vars.prj_namespace,
      // app_name: vars.paasify_stack,
      // app_fqdn: vars.paasify_stack + '.' + vars.app_domain,


      # Compose structure
      # --------------------------
      app_service: vars.stack_service,

      app_network: vars.stack_network,
      app_network_external: false,
      app_network_name: vars.prj_namespace + vars.paasify_sep + vars.stack_name,

      # App exposition
      # --------------------------
      app_expose: false,
      app_expose_ip: '0.0.0.0',
      app_expose_port: null,

      app_port: '80',
      app_prot: 'tcp',


      # App configuration
      # --------------------------

      app_puid: '1000',
      app_pgid: '1000',

      app_lang: 'en_US',
      app_tz: 'UTC',
      app_tz_var: 'TZ',
      app_tz_mount: false,
      app_tz_mounts: '/etc/timezone:/etc/timezone:ro,/etc/localtime:/etc/localtime:ro',

      app_debug: 'false',


      # App user informations
      # --------------------------

      app_admin_login: 'admin',
      app_admin_email: 'admin@' + self.app_domain,
      app_admin_passwd: 'admin',

      app_user_login: 'user',
      app_user_email: 'user@' + self.app_domain,
      app_user_passwd: 'user',


      # App directories
      # --------------------------

      # Usual app dirs
      app_dir_root: dir_prefix,
      app_dir_build: dir_prefix + 'build', # Build dir
      app_dir_script: dir_prefix + 'scripts', # Dir for storing container scripts and helpers 
      app_dir_secrets: dir_prefix + 'secrets', # Autogenerated secrets

      # Runtime dir
      app_dir_conf: dir_prefix + 'conf', # Commitables files into git
      app_dir_backup: dir_prefix + 'backup', # Backup directory
      app_dir_data: dir_prefix + 'data', # Backup data
      app_dir_share: dir_prefix + 'share', # No backup, data for apps

      # Temp dirs
      app_dir_cache: dir_prefix + 'cache', # Cache files
      app_dir_logs: dir_prefix + 'logs', # Backup ?
      app_dir_tmp: dir_prefix + 'tmp', # Just a tmp pool dir

      # Other dir helpers
      app_dir_db_data: dir_prefix + 'db_data', # Backup data
      app_dir_db_conf: dir_prefix + 'db_conf', # Commitables files into git



      # App Networks
      # --------------------------

      # Generic networks
      net_backup: vars.prj_namespace + vars.paasify_sep + 'backup', # For backup network
      net_docker: vars.prj_namespace + vars.paasify_sep + 'docker', # For docker socket access
      net_mail: vars.prj_namespace + vars.paasify_sep + 'mail',
      net_vpn: vars.prj_namespace + vars.paasify_sep + 'vpn',
      net_proxy: vars.prj_namespace + vars.paasify_sep + 'proxy',
      net_ldap: vars.prj_namespace + vars.paasify_sep + 'ldap',
      net_sql: vars.prj_namespace + vars.paasify_sep + 'sql', 
      net_nosql: vars.prj_namespace + vars.paasify_sep + 'nosql', 
      net_queue: vars.prj_namespace + vars.paasify_sep + 'queue', 
      net_ostorage: vars.prj_namespace + vars.paasify_sep + 'ostorage', # Object storage
      net_fstorage: vars.prj_namespace + vars.paasify_sep + 'fstorage', # File storage
      net_bstorage: vars.prj_namespace + vars.paasify_sep + 'bstorage', # Block storage
    
    },

  override_vars(vars):: 
    
    {
      app_fqdn: vars.app_name + '.' + vars.app_domain,
      // app_name: vars.paasify_stack,
      // app_fqdn: vars.paasify_stack + '.' + vars.app_domain,

    },

    // docker_override
  docker_override (vars, docker_file)::
    docker_file + {
      ["x-paasify-config"]: {
          new_custom_service: null,
        },
      // ["x-paasify-debug-vars"]: vars,
        
      },
    

};

paasify.main(plugin)